from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple


class BaseCipher(ABC):

    def __init__(self, **kwargs: Dict[str, str]) -> None:
        self.meta_data: List[Dict[str, Any]]
        self.entropy: float
        pass

    @abstractmethod
    def encode(self, text: str) -> str:
        pass

    @abstractmethod
    def decode(self, text: str) -> str:
        pass

    def cryptoanalis(self, text: str) -> Tuple[str, int, float, List[str]]:
        pass
