import random

class SelectingSystemParameters:
    """Выбор системных параметров"""

    def __init__(self, p, q, k, t):
        self.p = p
        self.q = q
        self.n = p * q
        self.k = k
        self.t = t

    @staticmethod
    def is_prime(l):
        """Проверка, является ли число простым"""
        if l <= 1:
            return False
        if l <= 3:
            return True
        if l % 2 == 0 or l % 3 == 0:
            return False
        i = 5
        while i * i <= l:
            if l % i == 0 or l % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def generate_prime():
        """Генерация простого числа"""
        num = random.randint(1, 999)
        while not SelectingSystemParameters.is_prime(num) or num % 4 != 3:
            num += 1
            if num > 999:
                num = 2
        return num

    @staticmethod
    def generate_n():
        """Генерация n"""
        p = SelectingSystemParameters.generate_prime()
        q = SelectingSystemParameters.generate_prime()
        return p * q

    @staticmethod
    def generate_security_params():
        """Выбор секретных параметров"""
        while True:
            k = random.randint(1, 18)
            print("\nСгенерированное k =", k)
            t = int(input("Введите кол-во раундов (t): "))
            if t > 0:
                return k, t
            print("Неверный ввод, t должно быть целым положительным числом")