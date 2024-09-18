import colorama
from colorama import Fore, Style
from example import str_examp

colorama.init()

# №1
colored_string: str = ''
for char in str_examp:
    if char == '#':
        colored_string += f'{Fore.GREEN}{char}{Style.RESET_ALL}'
    else:
        colored_string += char
print(colored_string)

# №2
print(str_examp.replace("#", f'{Fore.GREEN}#{Style.RESET_ALL}'))
