from typing import Any, Dict, List, Optional

from .BaseCipher import BaseCipher


class BitwiseCipher(BaseCipher):
    meta_data: List[Dict[str, Any]]

    def encode(self, text: str) -> str:
        encoded: str = ""
        self.meta_data = []
        for char in text:
            char_code: int = ord(char)
            left_byte: int = char_code >> 8
            right_byte: int = char_code & 0xFF
            encoded_char_code: int = ((left_byte ^ right_byte) << 8) | left_byte
            encoded += chr(encoded_char_code)
            self.meta_data.append(
                {
                    "Символ": char,
                    "Код 10": char_code,
                    "Код 2": bin(char_code),
                    "Левый байт": left_byte,
                    "Правый байт": right_byte,
                    "Код_ 10": encoded_char_code,
                    "Код_ 2": bin(encoded_char_code),
                    "Символ_": chr(encoded_char_code),
                }
            )
        return encoded

    def decode(self, text: str) -> str:
        decoded: str = ""
        self.meta_data = []
        for char in text:
            char_code: int = ord(char)
            left_byte: int = char_code >> 8
            right_byte: int = char_code & 0xFF
            decoded_char_code: int = (right_byte << 8) | (left_byte ^ right_byte)
            decoded += chr(decoded_char_code)
            self.meta_data.append(
                {
                    "Символ": char,
                    "Код 10": char_code,
                    "Код 2": bin(char_code),
                    "Левый байт": left_byte,
                    "Правый байт": right_byte,
                    "Код_ 10": decoded_char_code,
                    "Код_ 2": bin(decoded_char_code),
                    "Символ_": chr(decoded_char_code),
                }
            )
        return decoded
