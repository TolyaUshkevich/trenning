text_file = open('texsst.txt')
key = text_file.readline()
text = text_file.readline()
result = ''
key_letter_index = 0

while text != '':
    for text_letter in text:
        if ord(text_letter) <= 64 or ord(text_letter) > 123:
            result += text_letter
            continue

        if key_letter_index + 1 >= len(key):
            key_letter_index = 0
        key_letter = key[key_letter_index]

        if 64 < ord(text_letter) < 91:
            base_index = ord('A') - 1
        else:
            base_index = ord('a') - 1

        if (ord(key_letter) - base_index) + (ord(text_letter) - base_index) <= 26:
            result += chr(((ord(key_letter) - base_index) + (ord(text_letter) - base_index)) + base_index)
        elif (ord(key_letter) - base_index) + (ord(text_letter) - base_index) > 26:
            result += chr(((ord(key_letter) - base_index) + (ord(text_letter) - base_index) - 26) + base_index)

        key_letter_index += 1

    text = text_file.readline()

print(result)
