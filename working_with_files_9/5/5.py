with (open('surnames.txt', mode='r', encoding='UTF-8') as reader,
      open('woman.txt', mode='w', encoding='UTF-8') as writer_wom,
      open('man.txt', mode='w', encoding='UTF-8') as writer_man):
    content: list[str] = reader.readlines()

    fem_chars: list[str] = ['ВА', 'НА', 'АЯ']
    for name in content:
        last_letters: str = name.rstrip()[-2:]
        add_name: str = name.rstrip().capitalize() + '\n'

        if last_letters in fem_chars:
            writer_wom.write(add_name)
        else:
            writer_man.write(add_name)
