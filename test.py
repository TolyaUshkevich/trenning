def find_beautiful_numbers(num):

    len_num = len(str(num))
    counter = 0
    str_num = str(num)

    for i in range(len_num):
        if (i + 1) % 2 == 1:
            if int(str_num[i]) % 2 == 1:
                counter += 1
        if (i + 1) % 2 == 0:
            if int(str_num[i]) % 2 == 0:
                counter += 1

    if counter == len_num:
        return True
    else:
        return False






numb = int(input())
print(find_beautiful_numbers(numb))