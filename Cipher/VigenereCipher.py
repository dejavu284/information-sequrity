import math

from .BaseCipher import BaseCipher


class VigenereCipher(BaseCipher):

    def __init__(self, keyword: str) -> None:
        self.alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.alphabet_size = len(self.alphabet)
        self.keyword = keyword

    def encode(self, text: str) -> str:

        keyword_repeated = (self.keyword * (len(text) // len(self.keyword) + 1))[
            : len(text)
        ]
        encoded_text = ""

        for char, key_char in zip(text, keyword_repeated):
            shift = self.alphabet.index(key_char)
            encoded_text += self.shift_character(char, shift)

        self.entropy: float = self.calculate_entropy(encoded_text)

        return encoded_text

    def decode(self, text: str) -> str:

        keyword_repeated = (self.keyword * (len(text) // len(self.keyword) + 1))[
            : len(text)
        ]
        decoded_text = ""

        for char, key_char in zip(text, keyword_repeated):
            shift = self.alphabet.index(key_char)
            decoded_text += self.shift_character(char, -shift)

        self.entropy = self.calculate_entropy(decoded_text)

        return decoded_text

    def shift_character(self, char: str, shift: int) -> str:
        if char in self.alphabet:
            char_index = self.alphabet.index(char)
            return self.alphabet[(char_index + shift) % self.alphabet_size]
        else:
            return char

    def calculate_entropy(self, text: str) -> float:
        frequency = {}
        for char in text:
            if char in self.alphabet:
                if char not in frequency:
                    frequency[char] = 1
                else:
                    frequency[char] += 1

        entropy: float = 0.0
        total_chars = sum(frequency.values())
        for count in frequency.values():
            probability = count / total_chars
            if probability > 0:
                entropy -= probability * math.log2(probability)

        return round(entropy, 3)
