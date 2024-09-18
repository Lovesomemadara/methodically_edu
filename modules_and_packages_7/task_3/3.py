import pyfiglet
from font import text_font

# №1
font = pyfiglet.Figlet(font='digital')
line: str = 'Pentester'
art: str = font.renderText(line)
print(art)

# №2
print(text_font('Easy Task'))
