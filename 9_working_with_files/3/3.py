with (open('city.txt', mode='r', encoding='UTF-8') as reader,
      open('city_2.txt', mode='w', encoding='UTF-8') as writer):
    for line in reader.readlines():
        if 'о' not in line:
            writer.writelines(line)
