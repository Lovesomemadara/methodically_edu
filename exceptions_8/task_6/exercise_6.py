import random

from exceptions_8.get_number import get_num

rand_int: int = random.randint(1, 10)


def check_number(user_input: int):
    if user_input not in range(1, 11):
        return 'Ошибка Введите число от 1 до 10'

    if user_input < rand_int:
        return 'Ваше число меньше'
    else:
        return 'Ваше число больше'


if __name__ == '__main__':
    for _ in range(3):
        try:
            usr_inp: int = get_num('Введите число от 1 до 10: ')
        except ValueError:
            print('Ошибка! Вы ввели не число!')
        except (EOFError, KeyboardInterrupt) as err:
            print(err)
            break
        else:
            if usr_inp == rand_int:
                print('Ты победил!')
                break
            print(check_number(usr_inp))
    else:
        print('Удача не на твоей стороне, попробуй еще!')
