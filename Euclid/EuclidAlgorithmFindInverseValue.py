from math import floor, sqrt

from .EuclidAlgorithm import EuclidAlgorithm
from .EuclidAlgorithmFindLCD import EuclidAlgorithmFindLCD


class EuclidAlgorithmFindInverseValue(EuclidAlgorithm):
    def __init__(self, a: int, b: int) -> None:
        super().__init__(a, b)
        self.count_iterations = 20000

    def is_prime(self, number: int) -> bool:
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

    def calc(self) -> str:
        if self.is_prime(self.b):
            return "У числа нет обратного значения"

        simple_alg = EuclidAlgorithmFindLCD(self.a, self.b)
        if simple_alg.calc_digit() != 1:
            return "У числа нет обратного значения"

        v1, v2, v3 = 1, 0, self.a
        u1, u2, u3 = 0, 1, self.b
        incript = 0

        while u3 != 1 and incript < self.count_iterations:
            q = floor(u3 / v3)
            t1, t2, t3 = u1 - v1 * q, u2 - v2 * q, u3 - v3 * q
            u1, u2, u3 = v1, v2, v3
            v1, v2, v3 = t1, t2, t3
            incript += 1

        if incript >= self.count_iterations:
            return "Не удалось посчитать"
        else:
            return f"a^-1 = {u1 if u1 > 0 else self.b + u1}"
