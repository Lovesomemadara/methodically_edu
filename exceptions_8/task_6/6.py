import random

rand_int: int = random.randint(1, 10)

for attempt in range(3):
    try:
        user_input: int = int(input('Введите число от 1 до 10: '))
        MORE_LESS: str = (
            'Ваше число меньше'
            if user_input < rand_int
            else 'Ваше число больше'
            if user_input > rand_int
            else 'Ты победил!'
        )

        if not (1 <= user_input <= 10):
            print('Ошибка Введите число от 1 до 10')
            print(MORE_LESS)
        else:
            print(MORE_LESS)
            if user_input == rand_int:
                break
    except ValueError:
        print('Ошибка! Вы ввели не число!')
    except EOFError:
        print('Некорректное завершение программы')
        break
    except KeyboardInterrupt:
        print('\nОстановка выполнения программы')
        break
else:
    print('Удача не на твоей стороне, попробуй еще!')
