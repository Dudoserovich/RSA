import os
from math import sqrt
import random


class KeyGenerator:
    __p = int
    __q = int

    __public_key = ()
    __private_key = ()

    __root_dirname = 'rsa'

    def __init__(self, p: int, q: int):
        self.__p = p
        self.__q = q

    def __is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i <= sqrt(n):
            if n % i == 0:
                return False
            i = i + 2

        return True

    # очень глупый генератор (это далеко не самое лучшее решение)
    def __prime_generator(self, n):
        while True:
            n += 1
            if self.__is_prime(n):
                yield n

    def generate(self):
        n = self.__p * self.__q
        euler_function = (self.__p - 1) * (self.__q - 1)

        generator = self.__prime_generator(self.__p)
        random_simple_array = []
        for i in range(10):
            random_simple_array.append(next(generator))
        e = random.sample(random_simple_array, 1)[0]

        self.__public_key = (e, n)

        i = 0
        d = 0.1
        while d - int(d) != 0:
            d = (1 + (euler_function * i)) / e
            i += 1

        d = int(d)

        self.__private_key = (d, n)

    def save_keys(self):
        if not os.path.isdir(self.__root_dirname):
            os.mkdir(self.__root_dirname)
        public_key_file = open(f"./{self.__root_dirname}/rsa.pub", "w")
        public_key_file.write(str(self.__public_key[0]) + ' ' + str(self.__public_key[1]))

        private_key_file = open(f"./{self.__root_dirname}/rsa", "w")
        private_key_file.write(str(self.__private_key[0]) + ' ' + str(self.__private_key[1]))

    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key

    # @staticmethod
    # def read_public_key(self):
    #     self.__root_dirname