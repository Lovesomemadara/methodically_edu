import re
import string

from colorama import Fore, Style


def check_length():
    if len(password) not in range(8, 20):
        print("Ошибка! Длинна пароля должна быть от 8 до 20 символов!")
        return False

    return True


def first_capital():
    # if not re.match(r"^[A-Z]", password):
    #     print("Первая буква должна быть заглавной!")
    #     return False
    if not password[0].isupper():
        print("Первая буква должна быть заглавной!")
        return False

    return True
    # raise IndexError


def check_letters():
    # if not re.fullmatch(r"^[A-z0-9_]+[A-z0-9]$", password):
    #     print(
    #         "В пароле должны присутствовать только цифры, "
    #         "латинские буквы и нижнее подчеркивание"
    #     )
    #     return False
    allowed_chars: str = string.ascii_letters + string.digits
    for char in password:
        if char not in allowed_chars and "_" not in password:
            print(
                "В пароле должны присутствовать только цифры, "
                "латинские буквы и нижнее подчеркивание"
            )
            return False

    return True


def submit_pass():
    func_list: bool = all(
        [
            check_length(),
            first_capital(),
            check_letters(),
        ]
    )

    if func_list:
        return f"{Fore.GREEN} Пароль принят!{Style.RESET_ALL}"
    else:
        return (
            f"{Fore.RED} " "Пароль не соответствует требованиям! " f"{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    try:
        password: str = input("Введите пароль: ")
    except (IndexError, ValueError, TypeError, EOFError, KeyboardInterrupt) as err:
        print(err)
    else:
        print(submit_pass())
