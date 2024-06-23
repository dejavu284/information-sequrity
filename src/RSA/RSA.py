from typing import Optional, Tuple

import sympy


class RSA:
    def __init__(self, p: Optional[int] = None, q: Optional[int] = None) -> None:
        self.p: Optional[int] = p
        self.q: Optional[int] = q
        self.n: Optional[int] = None
        self.phi: Optional[int] = None
        self.e: Optional[int] = None
        self.d: Optional[int] = None

    def generate_keys(self, bit_length: int = 1024) -> Tuple[int, int, int, int, int]:
        if self.p is None or self.q is None:
            self.p = sympy.randprime(2 ** (bit_length // 2 - 1), 2 ** (bit_length // 2))
            self.q = sympy.randprime(2 ** (bit_length // 2 - 1), 2 ** (bit_length // 2))
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.choose_e(self.phi)
        self.d = self.modinv(self.e, self.phi)
        return self.p, self.q, self.n, self.e, self.d

    def choose_e(self, phi: int) -> int:
        e = 65537
        if sympy.gcd(e, phi) == 1:
            return e
        else:
            for e in range(3, phi, 2):
                if sympy.gcd(e, phi) == 1:
                    return e
        raise ValueError("Не удалось найти подходящее значение для e")

    def modinv(self, a: int, m: int) -> int:
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise ValueError("Нет обратного элемента")
        return x % m

    def egcd(self, a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        g, x1, y1 = self.egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    def encrypt(self, plaintext: int) -> int:
        if not self.e or not self.n:
            raise ValueError("Ключи не сгенерированы")
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext: int) -> int:
        if not self.d or not self.n:
            raise ValueError("Ключи не сгенерированы")
        return pow(ciphertext, self.d, self.n)
