text_file = open('texsst.txt')
count_of_nums = int(text_file.readline())
counter_of_numbers = 0
for i in range(count_of_nums):
    counter = 0
    number = int(text_file.readline())
    number = str(number)
    number = number[::-1]
    for i in range(len(number)):
        if (i + 1) % 2 == 0 and int(number[i]) % 2 == 0:
            counter += 1
        elif (i + 1) % 2 != 0 and int(number[i]) % 2 != 0:
            counter += 1
    if counter == len(number):
        counter_of_numbers += 1
print(counter_of_numbers)

