with open('city.txt', mode='r', encoding='UTF-8') as reader:
    line_count: int = 0
    for line in reader.readlines():
        line_count += 1

print(f'Количество строк в файле: {line_count}')
