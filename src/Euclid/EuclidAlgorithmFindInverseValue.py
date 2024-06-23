from math import sqrt
from typing import Union

from .EuclidAlgorithm import EuclidAlgorithm
from .EuclidAlgorithmDecomposition import EuclidAlgorithmDecomposition
from .EuclidAlgorithmFindLCD import EuclidAlgorithmFindLCD


class EuclidAlgorithmFindInverseValue(EuclidAlgorithm):
    def __init__(self, a: int, b: int) -> None:
        super().__init__(a, b)
        self.count_iteration = 20000

    def calc(self) -> Union[int, str]:
        gcd = EuclidAlgorithmFindLCD(self.A, self.B).calc()
        if gcd != 1:
            return "У числа нет обратного значения"

        alg = EuclidAlgorithmDecomposition(self.A, self.B)
        result = alg.calc()
        if isinstance(result, tuple):
            return result[0] if result[0] > 0 else self.B + result[0]
        else:
            return result
