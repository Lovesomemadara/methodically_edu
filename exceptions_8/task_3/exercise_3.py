def user_input_division(usr_inp: int, div_num: int) -> float:
    division: float = usr_inp / div_num
    return division


if __name__ == '__main__':
    inp, div = input('Введите число: '), input('Введите число: ')
    try:
        result: float = user_input_division(int(inp), int(div))
    except ZeroDivisionError:
        print('На ноль делить нельзя!\n'
              'Программа остановлена! '
              f'Поделить {inp} на {div} нельзя!')
    except (ValueError, TypeError):
        print('Возникла какая-то ошибка!\n'
              'Программа остановлена! '
              f'Поделить {inp} на {div} нельзя!')
    else:
        print(f'Результат деления равен: {result:.2f}')
