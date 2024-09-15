import time


# TODO: Улучшить

def timer(number: int):
    for num in range(number, -1, -1):
        print(f'\r{num}', end='')
        time.sleep(1)


def run():
    if not (10 < user_input < 30):
        print('Ошибка! Введите число от 10 до 30')
    else:
        try:
            timer(user_input)
        except ValueError:
            print('Синтаксическая ошибка')
        except EOFError:
            print('Некорректное завершение программы')
        except KeyboardInterrupt:
            print('\nОстановка выполнения программы')


if __name__ == '__main__':
    user_input: int = int(input('Введите число от 10 до 30: '))
