import time

user_input: int = int(input('Введите число от 10 до 30: '))

if not (10 < user_input < 30):
    print('Ошибка! Введите число от 10 до 30')
else:
    try:
        for num in range(user_input, -1, -1):
            print(f'\r{num}', end='')
            time.sleep(1)
    except ValueError:
        print('Синтаксическая ошибка')
    except EOFError:
        print('Некорректное завершение программы')
    except KeyboardInterrupt:
        print('\nОстановка выполнения программы')
