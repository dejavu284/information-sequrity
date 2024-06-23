import random


class RabinMiller:
    def __init__(self, iterations: int = 100) -> None:
        self.iterations = iterations

    def is_prime(self, n: int) -> bool:
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        # Найти s и t такие, что n-1 = 2^t * s, где s нечетно
        s = n - 1
        t = 0
        while s % 2 == 0:
            s //= 2
            t += 1

        # Провести тест заданное количество раз
        for _ in range(self.iterations):
            if not self._trial_composite(n, s, t):
                return False

        return True

    def _trial_composite(self, n: int, s: int, t: int) -> bool:
        b = random.randrange(2, n - 1)
        z = pow(b, s, n)
        if z == 1 or z == n - 1:
            return True

        for _ in range(t - 1):
            z = pow(z, 2, n)
            if z == n - 1:
                return True
            if z == 1:
                return False
        return False
