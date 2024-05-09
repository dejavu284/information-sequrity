import os
import sys
from typing import Any, Dict, List, Optional

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from Cipher import BitwiseCipher, CaesarsCipher, Context, VigenereCipher
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
        self.ui.key.setPlaceholderText(
            "Ключ должен состоять из ЗАГЛАВНЫХ букв русского алфавита"
        )
        self.ui.key_try.setPlaceholderText(
            "Ключ должен состоять из ЗАГЛАВНЫХ букв русского алфавита"
        )
        self.ui.key_try.setValidator(validator)

    def load(self) -> None:
        # Метод для открытия диалогового окна выбора файла
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
        # Метод для открытия диалогового окна выбора файла
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

    def update(self, objects: List[Any]) -> Any:
        current_index = self.ui.tabWidget.currentIndex()
        return objects[current_index]

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

        self.encode_button.disconnect()
        self.decode_button.disconnect()
        self.ui.caesars_cryptanalysis.disconnect()
        self.ui.bitwise_visualize.disconnect()
        self.ui.vigenere_visualize_entropy.disconnect()
        self.load_button.disconnect()
        self.save_button.disconnect()

        self.encode_button.clicked.connect(self.encode)
        self.decode_button.clicked.connect(self.decode)
        self.ui.caesars_cryptanalysis.clicked.connect(self.cryptanalysis)
        self.ui.bitwise_visualize.clicked.connect(self.visualize)
        self.ui.vigenere_visualize_entropy.clicked.connect(self.entropy)
        self.load_button.clicked.connect(self.load)
        self.save_button.clicked.connect(self.save)

    def encode(self) -> None:
        if self.cipher == CaesarsCipher:
            shift = self.ui.shift.text()
            self.context.set_cipher(self.cipher(shift))

        elif self.cipher == VigenereCipher:
            key = self.ui.key.text()
            if self.key_is_correct(key):
                key = key.upper().strip()
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
            shift = self.tryParse(self.ui.shift_try.text())
            self.context.set_cipher(self.cipher(shift))

        elif self.cipher == VigenereCipher:
            key = self.ui.key_try.text()
            if self.key_is_correct(key):
                key = key.upper().strip()
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

        # Установка заголовков столбцов
        self.ui.tableWidget.setHorizontalHeaderLabels(data_list[0].keys())

        # Заполнение таблицы данными
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

    def shift_is_correct(self, shift: int) -> bool:
        return shift != -1 and self.number_between(shift)

    def key_is_correct(self, key: str) -> bool:
        return key != "" and self.is_text(key)

    def is_text(self, text: str) -> bool:
        return False not in [
            True if char in self.ALPHABET else False
            for char in self.text_normalization(text)
        ]

    def is_not_empty(self, text: str) -> bool:
        return self.text_normalization(text) != ""

    def text_normalization(self, text: str) -> str:
        return text.upper().strip()

    def tryParse(self, string: str) -> int:
        try:
            return int(string)
        except ValueError:
            return -1

    def number_between(self, number: int) -> bool:
        return 1 <= number < 32


if __name__ == "__main__":
    print("Ok")
    app = QtWidgets.QApplication([])
    application = Gui()
    application.show()
    sys.exit(app.exec())
