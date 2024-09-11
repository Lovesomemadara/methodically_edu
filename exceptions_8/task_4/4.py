import animals
import random


def animals_choice(choice: int,
                   choice_of_animals: dict[int, dict[str, str]]) -> str:
    animal_name: str = list(choice_of_animals[choice].keys())[0]
    return choice_of_animals[choice][animal_name]


dict_of_animals: dict[int, dict[str, str]] = {
    1: {
        'deer': animals.deer
    },
    2: {
        'cat': animals.cat
    },
    3: {
        'cow': animals.cow
    },
    4: {
        'frog': animals.frog
    },
    5: {
        'bat': animals.bat
    },
    6: {
        'butterfly': animals.butterfly
    },
    7: {
        'random': random.choice([animals.butterfly, animals.bat,
                                 animals.frog, animals.deer,
                                 animals.cat, animals.cow])
    }
}


try:
    user_choice: int = int(input(' Help:\n\n'
                                 '\t\t1) deer\n'
                                 '\t\t2) cat\n'
                                 '\t\t3) cow\n'
                                 '\t\t4) frog\n'
                                 '\t\t5) bat\n'
                                 '\t\t6) butterfly\n'
                                 '\t\t7) random\n\n'
                                 ' Введите номер рисунка: '))
    if not (1 <= user_choice <= 7):
        print('Введите число от 1 до 7')
    else:
        print(animals_choice(user_choice, dict_of_animals))
except ValueError:
    print('Синтаксическая ошибка')
except EOFError:
    print('Некорректное завершение программы')
except KeyboardInterrupt:
    print('\nОстановка выполнения программы')
