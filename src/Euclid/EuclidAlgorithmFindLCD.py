from .EuclidAlgorithm import EuclidAlgorithm


class EuclidAlgorithmFindLCD(EuclidAlgorithm):
    def __init__(self, a: int, b: int) -> None:
        super().__init__(a, b)

    def calc(self) -> int:
        divisible, divider = self.A, self.B
        while divider != 0:
            divisible, divider = divider, divisible % divider
        return divisible
