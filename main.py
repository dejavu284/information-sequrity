import secrets
import sys
import time
from typing import Any, Dict, List, Tuple, Union

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from Cipher import BitwiseCipher, CaesarsCipher, Context, VigenereCipher
from Euclid import (
    EuclidAlgorithm,
    EuclidAlgorithmDecomposition,
    EuclidAlgorithmFindInverseValue,
    EuclidAlgorithmFindLCD,
)
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
            [self.ui.caesars_input, self.ui.vigenere_input, self.ui.bitwise_input]
        )
        self.output = self.update(
            [self.ui.caesars_output, self.ui.vigenere_output, self.ui.bitwise_output]
        )
        self.encode_button = self.update(
            [self.ui.caesars_encode, self.ui.vigenere_encode, self.ui.bitwise_encode]
        )
        self.decode_button = self.update(
            [self.ui.caesars_decode, self.ui.vigenere_decode, self.ui.bitwise_decode]
        )
        self.load_button = self.update(
            [self.ui.caesars_load, self.ui.vigenere_load, self.ui.bitwise_load]
        )
        self.save_button = self.update(
            [self.ui.caesars_save, self.ui.vigenere_save, self.ui.bitwise_save]
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
