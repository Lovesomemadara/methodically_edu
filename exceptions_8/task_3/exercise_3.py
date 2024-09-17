def user_input_division(usr_inp: int, div_num: int) -> float:
    division: float = int(usr_inp) / int(div_num)
    return division


if __name__ == '__main__':
    try:
        result: float = (
            user_input_division(
                inp := input('Введите число: '),
                div := input('Введите число: ')
            )
        )
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
