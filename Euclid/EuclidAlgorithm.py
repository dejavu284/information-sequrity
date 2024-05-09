from typing import Optional


class EuclidAlgorithm:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def calc(self) -> Optional[str]:
        raise NotImplementedError("This method should be overridden by subclasses")
