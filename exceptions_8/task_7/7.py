import re

from colorama import Fore, Style


def check_length():
    if len(password) not in range(8, 20):
        print(
            "Ошибка! Длинна пароля должна быть от 8 до 20 символов!",
        )
        return False

    return True


def first_capital():
    if not re.match(r"^[A-Z]", password):
        print("Первая буква должна быть заглавной!")
        return False

    return True


def check_letters():
    if not re.fullmatch(r"^[A-z0-9_]+[A-z0-9]$", password):
        print(
            "В пароле должны присутствовать только цифры, "
            "латинские буквы и нижнее подчеркивание"
        )
        return False

    return True


if __name__ == "__main__":
    try:
        password: str = input("Введите пароль: ")
        func_list: bool = all(
            [
                check_length(),
                first_capital(),
                check_letters(),
            ]
        )

        if func_list:
            print(f"{Fore.GREEN} Пароль принят!{Style.RESET_ALL}")
        else:
            print(
                f"{Fore.RED} "
                "Пароль не соответствует требованиям!"
                f"{Style.RESET_ALL}"
            )

    except ValueError:
        print("Ошибка. Некорректный ввод данных!")
    except TypeError:
        print("Несовместимый тип данных!")
    except NameError:
        print("Одно(некоторые) из имен не определено!")
    except AttributeError:
        print("Ошибка: Неверное использование библиотеки colorama!")
    except ImportError:
        print("Ошибка: Не удалось импортировать необходимые библиотеки!")
    except EOFError:
        print("Завершение программы через EOF!")
    except KeyboardInterrupt:
        print("\nОстановка выполнения программы!")
