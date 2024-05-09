from math import sqrt
from typing import Union

from .EuclidAlgorithm import EuclidAlgorithm
from .EuclidAlgorithmFindLCD import EuclidAlgorithmFindLCD


class EuclidAlgorithmFindInverseValue(EuclidAlgorithm):
    def __init__(self, a: int, b: int) -> None:
        super().__init__(a, b)
        self.count_iteration = 20000

    def calc(self) -> Union[int, str]:
        gcd = EuclidAlgorithmFindLCD(self.A, self.B).calc()
        if gcd != 1:
            return "У числа нет обратного значения"

        v1, v2, v3 = 1, 0, self.A
        u1, u2, u3 = 0, 1, self.B
        incript = 0

        while v3 != 0 and incript < self.count_iteration:
            q = u3 // v3
            t1, t2, t3 = u1 - v1 * q, u2 - v2 * q, u3 - v3 * q
            u1, u2, u3 = v1, v2, v3
            v1, v2, v3 = t1, t2, t3
            incript += 1

        if incript >= self.count_iteration:
            return "Не удалось посчитать"
        else:
            return u1 if u1 > 0 else self.B + u1

    @staticmethod
    def is_prime(number: int) -> bool:
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
