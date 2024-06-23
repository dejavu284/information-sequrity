import random
import secrets
import sys
import time
from typing import Any, Dict, List, Tuple, Union

import matplotlib.pyplot as plt
import sympy
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from sympy import randprime

from src.Cipher import BitwiseCipher, CaesarsCipher, Context, VigenereCipher
from src.Euclid import (
    EuclidAlgorithm,
    EuclidAlgorithmDecomposition,
    EuclidAlgorithmFindInverseValue,
    EuclidAlgorithmFindLCD,
)
from src.NLFSR import NLFSR
from src.Prime import RabinMiller
from src.RSA import RSA
from view.ui import Ui_MainWindow

# pyuic5.exe ui.ui -o ui.py

"""
GuiApps/
├── information_security/
│   ├── __init__.py
│   ├── main.py
│   └── Cipher/
│       ├── __init__.py
│       ├── BaseCipher.py
│       ├── BitwiseCipher.py
│       ├── CasearCipher.py
│       ├── VigenereCipher.py
"""


class Gui(QtWidgets.QMainWindow):

    ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def __init__(self) -> None:
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle("Шифр Цезаря")
        self.setWindowIcon(QtGui.QIcon(r"./view/icon-cipher-png"))

        self.context = Context()
        self.update_cipher()
        self.make_table()

        self.ui.tabWidget.currentChanged.connect(self.update_cipher)

        regex = QRegExp("[А-Я]+")
        validator = QRegExpValidator(regex)
        self.ui.key.setValidator(validator)
        self.ui.key.setPlaceholderText("ЗАГЛАВНЫЕ БУКВЫ")
        self.ui.key_try.setPlaceholderText("ЗАГЛАВНЫЕ БУКВЫ")
        self.ui.key_try.setValidator(validator)

        self.alg: EuclidAlgorithm

    def update(self, objects: List[Any]) -> Any:
        current_index = self.ui.tabWidget.currentIndex()
        return objects[current_index] if current_index < len(objects) else None

    def update_cipher(self) -> None:
        self.cipher = self.update([CaesarsCipher, VigenereCipher, BitwiseCipher])
        self.input = self.update(
            [
                self.ui.caesars_input,
                self.ui.vigenere_input,
                self.ui.bitwise_input,
                None,
                self.ui.start_state_input,
                None,
            ]
        )
        self.output = self.update(
            [
                self.ui.caesars_output,
                self.ui.vigenere_output,
                self.ui.bitwise_output,
                None,
                self.ui.output_text,
                None,
            ]
        )
        self.encode_button = self.update(
            [self.ui.caesars_encode, self.ui.vigenere_encode, self.ui.bitwise_encode]
        )
        self.decode_button = self.update(
            [self.ui.caesars_decode, self.ui.vigenere_decode, self.ui.bitwise_decode]
        )
        self.load_button = self.update(
            [
                self.ui.caesars_load,
                self.ui.vigenere_load,
                self.ui.bitwise_load,
                None,
                self.ui.load_start_state,
                None,
            ]
        )
        self.save_button = self.update(
            [
                self.ui.caesars_save,
                self.ui.vigenere_save,
                self.ui.bitwise_save,
                None,
                self.ui.save_result,
                None,
            ]
        )

        # Cipher disconnect
        if self.encode_button:
            self.encode_button.disconnect()
        if self.decode_button:
            self.decode_button.disconnect()
        if self.ui.caesars_cryptanalysis:
            self.ui.caesars_cryptanalysis.disconnect()
        if self.ui.bitwise_visualize:
            self.ui.bitwise_visualize.disconnect()
        if self.ui.vigenere_visualize_entropy:
            self.ui.vigenere_visualize_entropy.disconnect()
        if self.load_button:
            self.load_button.disconnect()
        if self.save_button:
            self.save_button.disconnect()

        # Euclid disconnect
        if self.ui.euclid_decompose_gcd:
            self.ui.euclid_decompose_gcd.disconnect()
        if self.ui.euclid_find_gcd:
            self.ui.euclid_find_gcd.disconnect()
        if self.ui.euclid_find_inverse:
            self.ui.euclid_find_inverse.disconnect()
        if self.ui.euclid_testing:
            self.ui.euclid_testing.disconnect()

        # NLFSR disconnect
        if self.ui.generate_start_state:
            self.ui.generate_start_state.disconnect()
        if self.ui.generate_nlfsr:
            self.ui.generate_nlfsr.disconnect()
        if self.ui.save_start_state:
            self.ui.save_start_state.disconnect()

        # Prime disconnect
        if self.ui.prime_check:
            self.ui.prime_check.disconnect()
        if self.ui.prime_testing:
            self.ui.prime_testing.disconnect()

        # RSA connect
        if self.ui.generate_keys_button:
            self.ui.generate_keys_button.disconnect()
        if self.ui.generate_primes_button:
            self.ui.generate_primes_button.disconnect()
        if self.ui.encrypt_message_button:
            self.ui.encrypt_message_button.disconnect()
        if self.ui.save_keys_button:
            self.ui.save_keys_button.disconnect()
        if self.ui.save_encrypted_message_button:
            self.ui.save_encrypted_message_button.disconnect()

        if self.ui.load_keys_button:
            self.ui.load_keys_button.disconnect()
        if self.ui.load_encrypted_message_button:
            self.ui.load_encrypted_message_button.disconnect()
        if self.ui.decrypt_message_button:
            self.ui.decrypt_message_button.disconnect()

        # Cipher connect
        if self.encode_button:
            self.encode_button.clicked.connect(self.encode)
        if self.decode_button:
            self.decode_button.clicked.connect(self.decode)
        if self.ui.caesars_cryptanalysis:
            self.ui.caesars_cryptanalysis.clicked.connect(self.cryptanalysis)
        if self.ui.bitwise_visualize:
            self.ui.bitwise_visualize.clicked.connect(self.visualize)
        if self.ui.vigenere_visualize_entropy:
            self.ui.vigenere_visualize_entropy.clicked.connect(self.entropy)
        if self.load_button:
            self.load_button.clicked.connect(self.load)
        if self.save_button:
            self.save_button.clicked.connect(self.save)

        # Euclid connect
        if self.ui.euclid_decompose_gcd:
            self.ui.euclid_decompose_gcd.clicked.connect(self.decompose_gcd)
        if self.ui.euclid_find_gcd:
            self.ui.euclid_find_gcd.clicked.connect(self.find_gcd)
        if self.ui.euclid_find_inverse:
            self.ui.euclid_find_inverse.clicked.connect(self.find_inverse)
        if self.ui.euclid_testing:
            self.ui.euclid_testing.clicked.connect(self.testing_euclid)

        # NLFSR connect
        if self.ui.generate_start_state:
            self.ui.generate_start_state.clicked.connect(self.generate_start_state)
        if self.ui.generate_nlfsr:
            self.ui.generate_nlfsr.clicked.connect(self.generate_and_display)
        if self.ui.save_start_state:
            self.ui.save_start_state.clicked.connect(self.save_seed)

        # Prime connect
        if self.ui.prime_check:
            self.ui.prime_check.clicked.connect(self.prime_check)
        if self.ui.prime_testing:
            self.ui.prime_testing.clicked.connect(self.prime_testing)

        # RSA connect
        if self.ui.generate_keys_button:
            self.ui.generate_keys_button.clicked.connect(self.generate_keys)
        if self.ui.generate_primes_button:
            self.ui.generate_primes_button.clicked.connect(self.generate_primes)
        if self.ui.encrypt_message_button:
            self.ui.encrypt_message_button.clicked.connect(self.encrypt_message)
        if self.ui.save_keys_button:
            self.ui.save_keys_button.clicked.connect(self.save_keys)
        if self.ui.save_encrypted_message_button:
            self.ui.save_encrypted_message_button.clicked.connect(
                self.save_encrypted_message
            )

        if self.ui.load_keys_button:
            self.ui.load_keys_button.clicked.connect(self.load_keys)
        if self.ui.load_encrypted_message_button:
            self.ui.load_encrypted_message_button.clicked.connect(
                self.load_encrypted_message
            )
        if self.ui.decrypt_message_button:
            self.ui.decrypt_message_button.clicked.connect(self.decrypt_message)

    def generate_primes(self):
        try:
            p = sympy.randprime(
                2**10, 2**11
            )  # Генерация простого числа с длиной в 10-11 бит
            q = sympy.randprime(2**10, 2**11)
            self.ui.prime_p.setText(str(p))
            self.ui.prime_q.setText(str(q))
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def generate_keys(self):
        try:
            p_text = self.ui.prime_p.text()
            q_text = self.ui.prime_q.text()

            if not p_text.isdigit() or not q_text.isdigit():
                raise ValueError("Числа p и q должны быть целыми числами")

            p = int(p_text)
            q = int(q_text)

            # Проверка, являются ли p и q простыми
            if not sympy.isprime(p):
                p = sympy.randprime(2**10, 2**11)
                self.ui.prime_p.setText(str(p))
            if not sympy.isprime(q):
                q = sympy.randprime(2**10, 2**11)
                self.ui.prime_q.setText(str(q))

            self.rsa = RSA(p, q)
            p, q, n, e, d = self.rsa.generate_keys()
            self.ui.public_n.setText(str(n))
            self.ui.phi_n.setText(str(self.rsa.phi))
            self.ui.public_e.setText(str(e))
            self.ui.private_d.setText(str(d))
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def encrypt_message(self):
        try:
            message_text = self.ui.message_to_encrypt.text()
            if not message_text.isdigit():
                raise ValueError("Сообщение для шифрования должно быть целым числом")
            message = int(message_text)
            ciphertext = self.rsa.encrypt(message)
            self.ui.encrypted_message.setText(str(ciphertext))
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def save_keys(self):
        try:
            n_text = self.ui.public_n.text()
            if not n_text.isdigit():
                raise ValueError("Ключ n должен быть целым числом")
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить ключи",
                "",
                "Text Files (*.txt);;All Files (*)",
                options=options,
            )
            if filename:
                with open(filename, "w") as file:
                    file.write(f"n: {n_text}\n")
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def save_encrypted_message(self):
        try:
            encrypted_message_text = self.ui.encrypted_message.text()
            if not encrypted_message_text.isdigit():
                raise ValueError("Зашифрованное сообщение должно быть целым числом")
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить зашифрованное сообщение",
                "",
                "Text Files (*.txt);;All Files (*)",
                options=options,
            )
            if filename:
                with open(filename, "w") as file:
                    file.write(encrypted_message_text)
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def load_keys(self):
        try:
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Загрузить ключи",
                "",
                "Text Files (*.txt);;All Files (*)",
                options=options,
            )
            if filename:
                with open(filename, "r") as file:
                    key_data = file.read().strip()
                    if not key_data.startswith("n: "):
                        raise ValueError("Некорректный формат файла ключей")

                    n_value = key_data.split(": ")[1].strip()
                    if not n_value.isdigit():
                        raise ValueError("Ключ n должен быть целым числом")

                    self.ui.receiver_public_n.setText(n_value)
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def load_encrypted_message(self):
        try:
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getOpenFileName(
                self,
                "Загрузить зашифрованное сообщение",
                "",
                "Text Files (*.txt);;All Files (*)",
                options=options,
            )
            if filename:
                with open(filename, "r") as file:
                    encrypted_message_text = file.read().strip()
                    if not encrypted_message_text.isdigit():
                        raise ValueError(
                            "Зашифрованное сообщение должно быть целым числом"
                        )
                    self.ui.receiver_encrypted_message.setText(encrypted_message_text)
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def decrypt_message(self):
        try:
            ciphertext_text = self.ui.receiver_encrypted_message.text()
            d_text = self.ui.receiver_private_d.text()
            n_text = self.ui.receiver_public_n.text()
            if (
                not ciphertext_text.isdigit()
                or not d_text.isdigit()
                or not n_text.isdigit()
            ):
                raise ValueError("Все значения должны быть целыми числами")
            ciphertext = int(ciphertext_text)
            d = int(d_text)
            n = int(n_text)
            self.rsa.d = d
            self.rsa.n = n
            plaintext = self.rsa.decrypt(ciphertext)
            self.ui.decrypted_message.setText(str(plaintext))
        except ValueError as ve:
            QMessageBox.critical(self, "Ошибка", str(ve))

    def generate_start_state(self) -> None:
        random_seed = random.getrandbits(32)
        self.ui.start_state_input.setText(hex(random_seed)[2:])

    def generate_and_display(self) -> None:
        seed_value = int(self.ui.start_state_input.text(), 16)
        iterations = int(self.ui.iterations_input.text())

        nlfsr = NLFSR(seed_value)

        self.ui.output_text.clear()
        self.ui.output_text.append("Generated:   Iteration #1\n")
        self.ui.output_text.append(f"             {seed_value:032b}\n")

        for i in range(2, iterations + 1):
            new_number = nlfsr.shift_and_xor()
            self.ui.output_text.append(f"Shifted:     Iteration #{i}\n")
            self.ui.output_text.append(f"             {new_number:032b}\n")

        remembered_bits = nlfsr.get_shifted_bits()
        self.ui.output_text.append("\nRemembered Bits: \n")
        self.ui.output_text.append("".join(str(bit) for bit in remembered_bits))

    def save_seed(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Выбрать текстовый файл",
            "./information_security/text",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if filename:
            with open(filename, "w", encoding="utf-8") as file:
                text = self.ui.start_state_input.text()
                file.write(text)

    def prime_check(self) -> None:
        input_number: int = int(self.ui.prime_input_number.text())
        alg = RabinMiller()
        is_prime = alg.is_prime(input_number)
        if is_prime:
            result = "Число простое"
        else:
            result = "Число не простое"
        self.ui.prime_result_output.setText(result)

    def prime_testing(self) -> None:
        def generate_primes(digits: int) -> int:
            """Генерация случайного простого числа заданной разрядности."""
            lower_bound = 10 ** (digits - 1)
            upper_bound = 10**digits - 1
            return randprime(lower_bound, upper_bound)

        alg = RabinMiller()
        digits_range = range(1, 6)
        times = {}
        result = ""
        for digits in digits_range:
            prime = generate_primes(digits)
            start_time = time.perf_counter()
            test_results = alg.is_prime(prime)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            times[digits] = elapsed_time
            is_prime = "Простое" if test_results else "Не простое"
            result += f"Разрядов: {digits}. Число: {prime} - {is_prime}. Длительность: {elapsed_time}\n\n"

        # Визуализация результатов
        plt.plot(list(times.keys()), list(times.values()), marker="x")
        plt.xlabel("Number of Digits")
        plt.ylabel("Average Time per Prime Check (s)")
        plt.title("Performance of Rabin-Miller Prime Test by Digits")
        plt.grid(True)
        print(self.ui.prime_visualize.isChecked())
        if self.ui.prime_visualize.isChecked():
            plt.show()

        self.ui.prime_testing_output.setText(result)

    def decompose_gcd(self) -> None:
        field_a: int = int(self.ui.field_A.text())
        field_b: int = int(self.ui.field_B.text())
        self.alg = EuclidAlgorithmDecomposition(a=field_a, b=field_b)
        result = self.alg.calc()
        decomposition = f"u1 = {result[0]}; u2 = {result[1]}; u3 = {result[2]};"
        self.ui.result_output.setText(decomposition)

    def find_inverse(self) -> None:
        field_a: int = int(self.ui.field_A.text())
        field_b: int = int(self.ui.field_B.text())
        self.alg = EuclidAlgorithmFindInverseValue(a=field_a, b=field_b)
        result = self.alg.calc()
        inverse_value = f"a^-1 = {result}"
        self.ui.result_output.setText(inverse_value)

    def find_gcd(self) -> None:
        field_a: int = int(self.ui.field_A.text())
        field_b: int = int(self.ui.field_B.text())
        self.alg = EuclidAlgorithmFindLCD(a=field_a, b=field_b)
        result = str(self.alg.calc())
        self.ui.result_output.setText(result)

    def testing_euclid(self) -> None:

        def next_by_number_digits(digits: int) -> int:
            max_value = 2**16 - 1
            if digits == 1:
                return secrets.randbelow(min(10, max_value))
            range_start = 10 ** (digits - 1)
            range_end = min((10**digits) - 1, max_value)
            return secrets.randbelow(range_end - range_start + 1) + range_start

        results: List[Tuple[int, int, int, Union[int, str], float]] = []
        for digits in range(1, 6):
            a = next_by_number_digits(digits)
            b = next_by_number_digits(digits)
            gcd_finder = EuclidAlgorithmFindLCD(a, b)
            iter = 0

            while gcd_finder.calc() != 1 & iter < 10000:
                b = next_by_number_digits(digits)
                gcd_finder = EuclidAlgorithmFindLCD(a, b)
                iter += 1

            if iter >= 10000:
                results.append((digits, a, b, "Нет обратного", 0.0))

            inverse_finder = EuclidAlgorithmFindInverseValue(a, b)
            start_time = time.time()
            result = inverse_finder.calc()
            end_time = time.time()

            elapsed_time = end_time - start_time
            results.append((digits, a, b, result, elapsed_time))

        testing_result = ""
        for res in results:
            testing_result += f"Digits: {res[0]}, A: {res[1]}, B: {res[2]}, Inverse: {res[3]}, Time: {res[4]:.6f} seconds\n\n"
        self.ui.testing_output.setText(testing_result)

    def load(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Выбрать текстовый файл",
            "./information_security/text",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if filename:
            with open(filename, "r", encoding="utf-8") as file:
                file_content = file.read().upper()
                self.input.setText(file_content)

    def save(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Выбрать текстовый файл",
            "./information_security/text",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if filename:
            with open(filename, "w", encoding="utf-8") as file:
                text = self.output.toPlainText()
                file.write(text)

    def encode(self) -> None:
        if self.cipher == CaesarsCipher:
            shift = self.ui.shift.text()
            self.context.set_cipher(self.cipher(shift))

        elif self.cipher == VigenereCipher:
            key = self.ui.key.text().upper().strip()
            self.context.set_cipher(self.cipher(key))

        elif self.cipher == BitwiseCipher:
            self.context.set_cipher(self.cipher())

        text = self.input.toPlainText().upper()
        if self.is_not_empty(text):
            self.context.set_text(text)
            encoded_text = self.context.encode()
            self.output.setText(encoded_text)
            self.decode_button.setEnabled(True)
            self.ui.caesars_cryptanalysis.setEnabled(True)
            self.ui.bitwise_visualize.setEnabled(True)

    def decode(self) -> None:
        if self.cipher == CaesarsCipher:
            shift = self.ui.shift_try.text()
            self.context.set_cipher(self.cipher(shift))

        elif self.cipher == VigenereCipher:
            key = self.ui.key_try.text().upper().strip()
            self.context.set_cipher(self.cipher(key))

        elif self.cipher == BitwiseCipher:
            self.context.set_cipher(self.cipher())

        encoded_text = self.output.toPlainText().upper()
        if self.is_not_empty(encoded_text):
            self.context.set_text(encoded_text)
            decoded_text = self.context.decode()
            self.output.setText(decoded_text)
            self.decode_button.setEnabled(False)
            self.ui.caesars_cryptanalysis.setEnabled(False)

    def cryptanalysis(self) -> None:
        if self.cipher == CaesarsCipher:
            self.context.set_cipher(self.cipher(1))

        encoded_text = self.output.toPlainText().upper()
        if self.is_not_empty(encoded_text):
            self.context.set_text(encoded_text)
            decoded_text = self.context.cryptanalysis()
            if decoded_text is None:
                return
            self.output.setText("\n\n".join(decoded_text))
            self.ui.caesars_cryptanalysis.setEnabled(False)
            self.decode_button.setEnabled(False)

    def visualize(self) -> None:
        if self.cipher == BitwiseCipher:
            if hasattr(self.context, "cipher"):
                if hasattr(self.context.cipher, "meta_data"):
                    self.fill_table(self.context.cipher.meta_data)

    def fill_table(self, data_list: List[Dict[str, Any]]) -> None:
        num_rows = len(data_list)
        num_columns = len(data_list[0])

        self.ui.tableWidget.setRowCount(num_rows)
        self.ui.tableWidget.setColumnCount(num_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(data_list[0].keys())

        for row, data_dict in enumerate(data_list):
            for column, key in enumerate(data_dict):
                item = QTableWidgetItem(str(data_dict[key]))
                self.ui.tableWidget.setItem(row, column, item)

    def make_table(self) -> None:
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "Символ",
                "Код 10",
                "Код 2",
                "Левый байт",
                "Правый байт",
                "Код_ 10",
                "Код_ 2",
                "Символ_",
            ]
        )
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.ui.tableWidget.verticalHeader().setVisible(False)

    def entropy(self) -> None:
        if self.cipher == VigenereCipher:
            if hasattr(self.context, "cipher"):
                if hasattr(self.context.cipher, "entropy"):
                    self.ui.vigenere_entropy.setText(str(self.context.cipher.entropy))

    def is_not_empty(self, text: str) -> bool:
        return self.text_normalization(text) != ""

    def text_normalization(self, text: str) -> str:
        return text.upper().strip()


if __name__ == "__main__":
    print("Ok")
    app = QtWidgets.QApplication([])
    application = Gui()
    application.show()
    sys.exit(app.exec())
