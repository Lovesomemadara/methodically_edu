import random
import time
from colorama import Fore, Style
from lorem_text import lorem


# TODO:
def countdown():
    for i in range(3, 0, -1):
        print(f'{i}...', end=' ')
        time.sleep(1)
    print(f'{Fore.RED}Начали!{Style.RESET_ALL}\n')


def generate_text():
    count_words: int = random.randint(5, 15)
    random_words: str = lorem.words(count_words)
    print(f'{Fore.CYAN}{random_words}{Style.RESET_ALL}\n')
    return random_words


def get_user_input() -> str:
    return input("Введите текст выше: ")


def display_statistics(start_time: float, end_time: float,
                       user_input: str, generated_text: str):
    elapsed_time: float = end_time - start_time
    words_per_minute: float = len(user_input.split()) / (elapsed_time / 60)

    if user_input == generated_text:
        print(f'\n{Fore.GREEN}####################################\n'
              f'###### Вы отлично справились! ######\n'
              f'###### Время печати: {round(elapsed_time, 1)} с.  ######\n'
              f'### Скорость печати: {round(words_per_minute, 1)} зн/м ####\n'
              f'####################################{Style.RESET_ALL}\n')
    else:
        print(
            f'{Fore.YELLOW} Увы, в тексте вы допустили ошибки'
            f'{Style.RESET_ALL}'
        )


def main():
    while True:
        print(f"{Fore.BLUE}if {Style.RESET_ALL}__name__ "
              f"{Fore.RED}=={Style.RESET_ALL} "
              f"{Fore.YELLOW}'__main__'{Style.RESET_ALL}:\n"
              f"\tmain()")

        countdown()
        generated_text: str = generate_text()

        start_time: float = time.time()
        user_input: str = get_user_input()
        end_time: float = time.time()

        display_statistics(start_time, end_time, user_input, generated_text)

        if user_input != generated_text:
            while True:
                retry = input(
                    'Начать заново(д) или завершить программу(н)? '
                ).strip().lower()
                match retry:
                    case 'д':
                        break
                    case 'н':
                        print('До новых встреч!')
                        exit()
                    case _:
                        print('Либо "д", либо "н".')


if __name__ == '__main__':
    main()
