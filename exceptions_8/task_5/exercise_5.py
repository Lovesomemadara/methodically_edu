import time

from exceptions_8.get_number import get_num


def timer(number: int):
    for num in range(number, -1, -1):
        print(f'\r{num}', end='')
        time.sleep(1)


def run(usr_inp: int):
    if not (10 < usr_inp < 30):
        print('Ошибка! Введите число от 10 до 30')
    else:
        return timer(usr_inp)


if __name__ == '__main__':
    try:
        run(get_num('Введите число от 10 до 30: '))
    except (ValueError, EOFError, KeyboardInterrupt) as err:
        print(err)
