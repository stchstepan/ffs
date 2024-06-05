import random
import math

class ProtocolMessages:
    """Один раунд"""

    @staticmethod
    def x_calculation(n, b):
        """A -> B"""
        r = random.randint(1, n - 1)
        b_random = int(random.choice(b))
        x = int((int(math.pow(-1, b_random)) * int(math.pow(r, 2)))% n)
        print("A отправляет x в сторону B...")
        return x, r

    @staticmethod
    def random_vector_generation(k):
        """B -> A"""
        e = []
        for i in range(1, k + 1):
            e_i = random.choice([0, 1])
            e.append(e_i)
        print("B отправляет e в сторону A...")
        return e

    @staticmethod
    def y_calculation(r, e, s, n):
        """A -> B"""
        s_e = dict(zip(s, e))
        s_in_e_all = [int(math.pow(key, value)) for key, value in s_e.items()]
        product_of_s_in_e = 1
        for i in s_in_e_all:
            product_of_s_in_e *= i
        y = int((r * product_of_s_in_e)% n)
        print("A отправляет y в сторону B...")
        return y

    @staticmethod
    def z_calculation(y, v, e, n):
        """B вычисляет z"""
        v_e = dict(zip(v, e))
        v_in_e_all = [int(math.pow(key, value)) for key, value in v_e.items()]
        product_of_v_in_e = 1
        for i in v_in_e_all:
            product_of_v_in_e *= i
        z = int((int(math.pow(y, 2)) * product_of_v_in_e) % n)
        return z

    @staticmethod
    def identification(x, z, n):
        """Выполнение идентификации"""
        return z != 0 and (z == x or z == -x % n)