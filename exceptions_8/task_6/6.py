import random

# TODO: Декомпозировать

rand_int: int = random.randint(1, 10)

for _ in range(3):

    try:
        user_input: int = int(input('Введите число от 1 до 10: '))
    except ValueError:
        print('Ошибка! Вы ввели не число!')
    except EOFError:
        print('Некорректное завершение программы')
        break
    except KeyboardInterrupt:
        print('\nОстановка выполнения программы')
        break
    else:
        if user_input == rand_int:
            print('Ты победил!')
            break

        if user_input not in range(1, 11):
            print('Ошибка Введите число от 1 до 10')

        if user_input < rand_int:
            print('Ваше число меньше')
        else:
            print('Ваше число больше')
else:
    print('Удача не на твоей стороне, попробуй еще!')
