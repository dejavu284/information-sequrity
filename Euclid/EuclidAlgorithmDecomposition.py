from math import floor

from .EuclidAlgorithm import EuclidAlgorithm


class EuclidAlgorithmDecomposition(EuclidAlgorithm):
    def __init__(self, a: int, b: int) -> None:
        super().__init__(a, b)
        self.count_iterations = 10000

    def calc(self) -> str:
        v1, v2, v3 = 1, 0, self.a
        u1, u2, u3 = 0, 1, self.b
        incript = 0

        while v3 != 0 and incript < self.count_iterations:
            q = floor(u3 / v3)
            t1, t2, t3 = u1 - v1 * q, u2 - v2 * q, u3 - v3 * q
            u1, u2, u3 = v1, v2, v3
            v1, v2, v3 = t1, t2, t3
            incript += 1

        if incript >= self.count_iterations:
            return "Не удалось посчитать"
        else:
            return f"u1 = {u1}; u2 = {u2}; u3 = {u3};"
