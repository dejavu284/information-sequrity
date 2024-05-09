from typing import List, Tuple

from .BaseCipher import BaseCipher


class CaesarsCipher(BaseCipher):
    def __init__(self, shift: int) -> None:
        self.shift: int = int(shift)
        self.alphabet: str = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.alphabet_size: int = len(self.alphabet)

    def encode(self, text: str) -> str:
        result: str = ""
        for char in text:
            if char in self.alphabet:
                index: int = self.alphabet.index(char)
                new_index: int = (index + self.shift) % self.alphabet_size
                result += self.alphabet[new_index]
            else:
                result += char
        return result

    def decode(self, text: str) -> str:
        result: str = ""
        for char in text:
            if char in self.alphabet:
                index: int = self.alphabet.index(char)
                new_index: int = (index - self.shift) % self.alphabet_size
                result += self.alphabet[new_index]
            else:
                result += char
        return result

    def cryptoanalis(self, text: str) -> Tuple[str, int, float, List[str]]:
        from typing import Dict

        FREQUENCIES: Dict[str, float] = {
            "А": 0.08,
            "Б": 0.016,
            "В": 0.045,
            "Г": 0.017,
            "Д": 0.03,
            "Е": 0.085,
            "Ж": 0.01,
            "З": 0.016,
            "И": 0.073,
            "Й": 0.012,
            "К": 0.034,
            "Л": 0.044,
            "М": 0.032,
            "Н": 0.067,
            "О": 0.11,
            "П": 0.028,
            "Р": 0.047,
            "С": 0.054,
            "Т": 0.063,
            "У": 0.026,
            "Ф": 0.0026,
            "Х": 0.0094,
            "Ц": 0.0048,
            "Ч": 0.014,
            "Ш": 0.007,
            "Щ": 0.0036,
            "Ъ": 0.00037,
            "Ы": 0.019,
            "Ь": 0.017,
            "Э": 0.0032,
            "Ю": 0.0064,
            "Я": 0.020,
        }

        def calculate_fitness(text: str) -> float:
            fitness: float = 0
            text_length: int = sum(text.count(letter) for letter in FREQUENCIES)
            for letter, frequency in FREQUENCIES.items():
                if text_length > 0:
                    text_frequency: int = text.count(letter)
                    fitness += abs(frequency * len(text) - text_frequency)
            return round(fitness, 3)

        best_fit: float = float("inf")
        best_text: str = ""
        best_key: int = 0
        decrypted_texts: List[str] = []
        for key in range(1, 33):  # Перебор возможных ключей от 1 до 32
            self.shift = key
            decrypted_text: str = self.decode(text)
            fitness: float = calculate_fitness(decrypted_text)
            decrypted_texts.append(f"{key} - {decrypted_text} - {fitness}")
            if fitness < best_fit:
                best_fit = fitness
                best_text = decrypted_text
                best_key = key
        return best_text, best_key, best_fit, decrypted_texts
