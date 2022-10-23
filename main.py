from termcolor import colored

from KeyGenerator import KeyGenerator
from TerminalStrategy import ConcreteStrategyA, Context, ConcreteStrategyB

if __name__ == "__main__":
    public_key = ()
    private_key = ()
    key_generator = KeyGenerator(0, 0)
    while True:
        try:
            print('Сгенерировать ключи? \ny - сгенерировать ключи, n - считать ключи из файлов:')
            question = input()

            context = Context(ConcreteStrategyA())
            if question == 'y':
                p, q = context.do_some_business_logic()

                key_generator = KeyGenerator(p, q)
                key_generator.generate()
                key_generator.save_keys()
                break
            elif question == 'n':
                private_key_file = open("rsa/rsa", "r")
                public_key_file = open("rsa/rsa.pub", "r")

                public_key = tuple(map(int, private_key_file.readline().split(' ')))
                private_key = tuple(map(int, public_key_file.readline().split(' ')))

                private_key_file.close()
                public_key_file.close()

                print(public_key, private_key)
                break
        except Exception as err:
            print(colored(str(err), 'red'))

    while True:
        try:
            print('Зашифровать/дешифровать сообщение (0, 1):')
            question = int(input())
            if question == 0:
                context.strategy = ConcreteStrategyB()
                message = context.do_some_business_logic()

                encoded_message = []
                e, n = key_generator.get_public_key() if not public_key else public_key

                for i in range(len(message)):
                    encoded_message.append(pow(ord(message[i]), e) % n)

                print('encoded message:', encoded_message)
                text_file = open("./rsa/encoded_message", "w")
                text_file.write(' '.join(map(str, encoded_message)))
                break
            elif question == 1:
                encoded_message_file = open("rsa/encoded_message", "r")
                encoded_message = map(int, encoded_message_file.readline().split(' '))

                print('-' * 5 + '3. Дешифрование сообщения' + '-' * 5)
                d, n = key_generator.get_private_key() if not private_key else private_key
                decoded_message = []
                for char in encoded_message:
                    decoded_message.append(chr(pow(char, d) % n))

                print(''.join(decoded_message))
                text_file = open("./rsa/decoded_message", "w")
                text_file.write(' '.join(map(str, decoded_message)))
                break
        except Exception as err:
            print(colored(str(err), 'red'))