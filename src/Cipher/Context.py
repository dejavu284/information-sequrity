from typing import List, Optional

from .BaseCipher import BaseCipher


class Context:

    def set_cipher(self, cipher: BaseCipher) -> None:
        self.cipher = cipher

    def set_text(self, text: str) -> None:
        self.text = text

    def del_cipher(self) -> None:
        if hasattr(self, "cipher"):
            del self.cipher

    def encode(self) -> Optional[str]:
        if hasattr(self, "text") and hasattr(self, "cipher"):
            self.encoded_text = self.cipher.encode(self.text)
            return self.encoded_text
        return None

    def decode(self) -> Optional[str]:
        if hasattr(self, "text") and hasattr(self, "cipher"):
            decoded_text = self.cipher.decode(self.text)
            return decoded_text
        return None

    def cryptanalysis(self) -> Optional[List[str]]:
        if (
            hasattr(self, "text")
            and hasattr(self, "cipher")
            and hasattr(self.cipher, "cryptoanalis")
        ):
            best_text, best_key, best_fit, decoded_texts = self.cipher.cryptoanalis(
                self.text
            )
            decoded_texts.append(
                f"\nРезультат криптоанализа:\n\n{best_key} - {best_text} - {best_fit}"
            )
            return decoded_texts
        return None
