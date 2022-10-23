from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from math import sqrt
import random
from termcolor import colored

from KeyGenerator import KeyGenerator


class Context():

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> List | str:
        return self._strategy.input_script()


class Strategy(ABC):
    @abstractmethod
    def input_script(self):
        pass

    @staticmethod
    def _is_prime(n: int) -> bool:
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

    @staticmethod
    def _eratosthenes(n=999) -> set[int]:
        a = []
        for i in range(n + 1):
            a.append(i)

        a[1] = 0

        i = 2
        while i <= n:
            if a[i] != 0:
                j = i + i
                while j <= n:
                    a[j] = 0
                    j = j + i
            i += 1

        a = set(a)
        a.remove(0)

        return a


class ConcreteStrategyA(Strategy):
    def input_script(self) -> List:
        array_simple = list(self._eratosthenes(333))[4::]
        p, q = [int, int]
        while True:
            try:
                print('-' * 5 + '1. Генерация ключей' + '-' * 5)
                print(
                    'Вы хотите автоматически сгенерировать p и q или ввести вручную? (0 - автоматическая генерация, 1 - ввести вручную)')
                what_do = int(input())
                if what_do not in [0, 1]:
                    continue
                if what_do == 0:
                    p, q = random.sample(array_simple, 2)
                    return [p, q]
                else:
                    print('Введите 2-х/3-х значные p и q:')
                    p, q = map(int, input().split())
                    if (p < 37 or p > 999) or (q < 37 or q > 999) or p == q:
                        raise Exception(
                            'Введено не 2-х/3-х значное число (минимальное допустимое число 37, т.к. в русском алфавите 33 буквы) или же числа одинаковые')
                    elif not self._is_prime(p) or not self._is_prime(q):
                        raise Exception('Как минимум одно из чисел не является простым')
                    return [p, q]
            except Exception as err:
                print(colored(str(err), 'red'))


class ConcreteStrategyB(Strategy):
    def input_script(self) -> str:
        while True:
            try:
                print('-' * 5 + '2. Шифрование сообщения' + '-' * 5)
                print('Введите сообщение, которое необходимо зашифровать:')
                return input()
            except Exception as err:
                print(colored(str(err), 'red'))


# if __name__ == "__main__":

# context = Context(ConcreteStrategyA())
# p, q = context.do_some_business_logic()
#
# key_generator = KeyGenerator(p, q)
# key_generator.generate()
#
# context.strategy = ConcreteStrategyB()
# message = context.do_some_business_logic()
#
# decoded_message = []
# e, n = key_generator.get_public_key()
#
# for i in range(len(message)):
#     decoded_message.append(pow(ord(message[i]), e) % n)
#
# print('decoded message:', decoded_message)
#
# print('-' * 5 + '3. Дешифрование сообщения' + '-' * 5)
# d, n = key_generator.get_private_key()
# encoded_message = []
# for char in decoded_message:
#     encoded_message.append(chr(pow(char, d) % n))
#
# print(''.join(encoded_message))