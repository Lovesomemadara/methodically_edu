# TODO: Разбить на блоки try except

def user_input_division(usr_inp: int, div_num: int):
    try:
        result: float = int(usr_inp) / int(div_num)
    except ZeroDivisionError:
        print('На ноль делить нельзя!\n'
              'Программа остановлена! '
              f'Поделить {usr_inp} на {div_num} нельзя!')
    except (ValueError, TypeError):
        print('Возникла ошибка с вводом данных!\n'
              'Программа остановлена! '
              f'Поделить {usr_inp} на {div_num} нельзя!')
    else:
        return print(f'Результат деления равен: {result:.2f}')


user_input_division(input('Введите число: '), input('Введите число: '))
