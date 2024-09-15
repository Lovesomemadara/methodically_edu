import random

# TODO: Декомпозировать

flag: bool = True
while flag:
    try:
        input_num: int = int(input('Введите число от 1 до 10: '))
    # except (ValueError, EOFError, KeyboardInterrupt) as err:
    #     print(err)

    except ValueError:
        print('Вы ввели строковое значение!')
    except EOFError:
        flag = False
        print('Программа завершена через "end_of_file".')
    except KeyboardInterrupt:
        print('\nЗавершите программу правильно.')
    else:
        if not (1 <= input_num <= 10):
            print('Введите число от 1 до 10!')
        else:
            rand_int: int = random.randint(10, 100)
            flag = False
            print(f' {sum(range(input_num, rand_int + 1))}')
