import colorama
from colorama import Fore, Style
from example import str_examp
colorama.init()

colored_string: str = ''
for char in str_examp:
    if char == '#':
        colored_string += f'{Fore.GREEN}{char}{Style.RESET_ALL}'
    else:
        colored_string += char

print(colored_string)

colorama.deinit()
