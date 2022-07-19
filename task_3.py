text_file = open('texsst.txt')
key = text_file.readline()
text = text_file.readline()
result = ''
counter = 0
let = ''
while text != '':
    if text != '':
        for s in text:
            if 64 < ord(s) < 123:
                if counter + 1 >= len(key):
                    counter = 0
                let = key[counter]
                if 64 < ord(s) < 91:
                    s = s.lower()
                    if (ord(let) - 96) + (ord(s) - 96) <= 26:
                        result += chr(((ord(let) - 96) + (ord(s) - 96)) + 96).upper()
                    elif (ord(let) - 96) + (ord(s) - 96) > 26:
                        result += chr(((ord(let) - 96) + (ord(s) - 96) - 26) + 96).upper()
                else:
                    if counter + 1 >= len(key):
                        counter = 0
                    let = key[counter]
                    if ord(let) - 96 > 0 and ord(s) - 96 > 0:
                        if (ord(let) - 96) + (ord(s) - 96) <= 26:
                            result += chr(((ord(let) - 96) + (ord(s) - 96)) + 96)
                        elif (ord(let) - 96) + (ord(s) - 96) > 26:
                            result += chr(((ord(let) - 96) + (ord(s) - 96) - 26) + 96)
                let = ''
                counter += 1
            else:
                result += s
        text = text_file.readline()



print(result)
