from abc import ABC, abstractmethod
from typing import Tuple, Union


class EuclidAlgorithm(ABC):
    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b

    @property
    def A(self) -> int:
        return self._a

    @A.setter
    def A(self, value: int) -> None:
        self._a = value

    @property
    def B(self) -> int:
        return self._b

    @B.setter
    def B(self, value: int) -> None:
        self._b = value

    @abstractmethod
    def calc(self) -> Union[str, int, Tuple[int, int, int]]:
        pass
