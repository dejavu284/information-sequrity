from typing import List


class NLFSR:
    def __init__(self, seed: int) -> None:
        self.register = seed
        self.shifted_bits = []

    def shift_and_xor(self) -> int:
        # Нелинейная функция: (b32 AND b31) XOR (b9 AND b2) XOR b0
        and_bits1 = ((self.register >> 31) & 1) & ((self.register >> 30) & 1)
        and_bits2 = ((self.register >> 8) & 1) & ((self.register >> 1) & 1)
        xor_bit = (self.register >> 0) & 1
        new_bit = and_bits1 ^ and_bits2 ^ xor_bit

        # Сдвиг числа и добавление нового бита
        new_number = (self.register >> 1) | (new_bit << 31)

        # Запоминаем младший бит
        self.shifted_bits.append(self.register & 1)

        # Обновляем регистр
        self.register = new_number

        return new_number

    def get_shifted_bits(self) -> List[int]:
        return self.shifted_bits

    def set_seed(self, seed: int) -> None:
        self.register = seed
        self.shifted_bits = []
