with open('city.txt', mode='r', encoding='UTF-8') as reader:
    line_count: int = len(reader.readlines())

print(f'Количество строк в файле: {line_count}')
