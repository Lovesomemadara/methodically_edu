with open('numbers.txt', mode='w', encoding='UTF-8') as writer:
    for i in range(1, 10001):
        writer.writelines(str(i) + '\n')

writer = open('numbers.txt', mode='w', encoding='UTF-8')
nums: list[str] = [str(i) for i in range(1, 10001)]
writer.writelines('\n'.join(nums))
writer.close()
