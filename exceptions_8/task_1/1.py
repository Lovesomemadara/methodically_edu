def get_number():
    while True:
        try:
            num = int(input("Введите число: "))
            if 10 <= num <= 20:
                print(f'Работаем с число {num}')
                return num
            else:
                print("Ошибка! Вы ввели не число или число не в диапазоне!")
        except ValueError:
            print("Ошибка! Вы ввели не число или число не в диапазоне!")


get_number()
