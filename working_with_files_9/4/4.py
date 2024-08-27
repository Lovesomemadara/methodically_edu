# decoded_string = b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb9'
# print(decoded_string.decode('UTF-8'))

with open('decode.txt', 'rb') as file:
    content = file.readlines()
    lines: list[bytes] = []
    for line in content:
        lines.append(line.rstrip())

    for word in lines:
        print(word.decode('UTF-8'))
