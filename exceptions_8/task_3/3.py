def user_input_division(usr_inp: int | str | float,
                        div_num: int | str | float):
    try:
        result: int | float = int(usr_inp) / int(div_num)
        return print(f'Результат деления равен: {result:.2f}')

    except ZeroDivisionError:
        print('На ноль делить нельзя!\n'
              f'Программа остановлена! '
              f'Поделить {usr_inp} на {div_num} нельзя!')
    except ValueError:
        print('Возникла какая то ошибка!\n'
              f'Программа остановлена! '
              f'Поделить {usr_inp} на {div_num} нельзя!')


user_input_division(input('Введите число: '), input('Введите число: '))
