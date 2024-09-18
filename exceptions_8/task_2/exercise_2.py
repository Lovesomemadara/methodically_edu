import random

from exceptions_8.get_number import get_num


def check_number():
    if 1 <= (num := get_num('Введите число от 1 до 10: ')) <= 10:
        rand_int: int = random.randint(10, 100)
        return sum(range(num, rand_int + 1))
    raise ValueError('Введите число от 1 до 10!')


if __name__ == '__main__':
    while True:
        try:
            result: int = check_number()
        except (ValueError, EOFError, KeyboardInterrupt) as err:
            print(err)
        else:
            print(result)
            break
