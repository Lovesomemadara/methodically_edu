import pyfiglet


def text_font(text: str, font_style: str = 'digital') -> str:
    font = pyfiglet.Figlet(font=font_style)
    art: str = font.renderText(text)
    return art
