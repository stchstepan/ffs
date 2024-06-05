import random
import math

class SelectingUserSecrets:
    """Выбор секретов пользователя"""

    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.s = []
        self.b = []
        self.v = []

    def select_user_secrets(self):
        """Выбор S_i и b_i"""
        for i in range(1, self.k + 1):
            s_i = 0
            while math.gcd(s_i, self.n) != 1:
                s_i = random.randint(1, self.n - 1)
            self.s.append(s_i)

        for i in range(1, self.k + 1):
            self.b.append(random.randint(0, 1))

        return self.s, self.b

    @staticmethod
    def extended_gcd(a, b):
        """Вычисление наибольшего общего делителя по расширенному алгоритму
        Евклида"""
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = SelectingUserSecrets.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    @staticmethod
    def mod_inverse(a, m):
        """Нахождение обратного по модулю числа"""
        gcd, x, y = SelectingUserSecrets.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError(f"Для {a} по модулю {m} обратного числа не существует")
        else:
            return (x % m + m) % m

    def v_calculation(self):
        """Вычисление v"""
        s_n_dict = dict(zip(self.s, self.b))
        self.v = []
        for key, value in s_n_dict.items():
            inverse = int(SelectingUserSecrets.mod_inverse(math.pow(key, 2), self.n))
            v_i = int(math.pow(-1, value)) * inverse % self.n
            self.v.append(v_i)
        return self.v

    def keys(self):
        """Формирование ключей"""
        open_key = [self.v, self.n]
        close_key = self.s
        return open_key, close_key
    
class Hacker:
    """Генерация случайного закрытого ключа"""

    def __init__(self, n, k, v):
        self.n = n
        self.k = k
        self.s = []
        self.v = v
    
    def hacker_generates_s(self):
        """Попытка ложной аутентфикации"""
        self.s = []
        for i in range(1, self.k + 1):
            s_i = random.randint(1, self.n - 1)
            self.s.append(s_i)
        return self.s
    
    def keys(self):
        """Формирование ключей"""
        open_key = [self.v, self.n]
        close_key = self.s
        return open_key, close_key