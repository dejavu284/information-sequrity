from typing import Optional

from .EuclidAlgorithm import EuclidAlgorithm


class EuclidAlgorithmFindLCD(EuclidAlgorithm):
    def calc(self) -> str:
        remains, previous_remains = self.b, None
        divisible, divider = self.a, self.b
        i = 0

        while remains > 0 and i < 1000:
            previous_remains = remains
            remains = divisible % divider
            divisible, divider = divider, remains
            i += 1

        if i >= 1000:
            return "Не удалось посчитать"
        return str(previous_remains)

    def calc_digit(self) -> Optional[int]:
        remains, previous_remains = self.b, None
        divisible, divider = self.a, self.b

        while remains > 0:
            previous_remains = remains
            remains = divisible % divider
            divisible, divider = divider, remains

        return previous_remains
