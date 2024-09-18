with (open('surnames.txt', mode='r', encoding='UTF-8') as reader,
      open('woman.txt', mode='w', encoding='UTF-8') as writer_wom,
      open('man.txt', mode='w', encoding='UTF-8') as writer_man):
    content: list[str] = reader.readlines()

    fem_chars: list[str] = ['ВА', 'НА', 'АЯ']
    women: list[str] = []
    men: list[str] = []

    for name in content:
        last_letters: str = name.rstrip()[-2:]
        add_name: str = name.rstrip().capitalize()

        if last_letters in fem_chars:
            women.append(add_name)
        else:
            men.append(add_name)

    # [
    #     women.append(name.rstrip().capitalize())
    #     if name.rstrip()[-2:] in fem_chars
    #     else men.append(name.rstrip().capitalize())
    #     for name in content
    # ]

    writer_wom.write('\n'.join(women))
    writer_man.write('\n'.join(men))
