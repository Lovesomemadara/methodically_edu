import pyfiglet


def text_font(text: str) -> str:
    font = pyfiglet.Figlet(font='digital')
    art: str = font.renderText(text)
    return art
