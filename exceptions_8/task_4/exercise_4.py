import random

import animals
from exceptions_8.get_number import get_num

names: list[str] = [
    "deer",
    "cat",
    "cow",
    "frog",
    "bat",
    "butterfly",
    "random",
]
pictures: list[str] = [
    animals.deer,
    animals.cat,
    animals.cow,
    animals.frog,
    animals.bat,
    animals.butterfly,
]
dict_of_animals: dict[str, str] = dict(zip(names, pictures))


def print_info():
    print(" Help:\n")
    for num, name in enumerate(names, 1):
        print(f"\t\t{num}) {name}")


def animals_choice(choice: int, choice_of_animals: dict[str, str]) -> str:
    if not (1 <= choice <= 7):
        raise ValueError("Введите число от 1 до 7!")

    if choice == 7:
        return random.choice(pictures)

    return choice_of_animals[names[choice - 1]]
    # return choice_of_animals.get(names[choice - 1], None)


if __name__ == "__main__":
    print_info()
    try:
        user_choice: int = get_num("\n Введите номер рисунка: ")
    except (ValueError, EOFError, KeyboardInterrupt) as err:
        print(err)
    else:
        print(animals_choice(user_choice, dict_of_animals))
