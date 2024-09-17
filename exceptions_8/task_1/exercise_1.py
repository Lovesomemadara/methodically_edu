from exceptions_8.get_number import get_num


def check_number() -> str:
    """Text.
    :raise ValueError:
    """
    if 10 <= (num := get_num("Введите число: ")) <= 20:
        return f"Работаем с число {num}"
    raise ValueError


if __name__ == "__main__":
    while True:
        try:
            result: str = check_number()
        except ValueError:
            print("Ошибка! Вы ввели не число или число не в диапазоне!")
        else:
            print(result)
            break
