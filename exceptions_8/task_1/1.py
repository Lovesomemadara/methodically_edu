def get_number() -> str:
    """Text.
    :raise ValueError:
    """
    if 10 <= (num := int(input("Введите число: "))) <= 20:
        return f"Работаем с число {num}"
    raise ValueError


if __name__ == "__main__":
    while True:
        try:
            res = get_number()
        except ValueError:
            print("Ошибка! Вы ввели не число или число не в диапазоне!")
        else:
            print(res)
            break
