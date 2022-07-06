
def count_seanses(len_of_working, time_from_last_cleaning, len_of_seans, len_of_cleaning):
    count_of_time = 0
    count_of_etaretions = 0
    count_of_seans = 0
    while count_of_time < len_of_working:
        while count_of_etaretions < time_from_last_cleaning:
            count_of_time += len_of_seans
            count_of_seans += 1
            count_of_etaretions += len_of_seans
            if count_of_time >= len_of_working:
                break

        count_of_etaretions = 0
        count_of_time += len_of_cleaning
        if count_of_time + len_of_seans > len_of_working:
            break
    return f'При данных условиях, за {len_of_working} минут, в день будет проводиться {count_of_seans} сенсов.'


# now I'm absolutely sure that that works:)


text_file = open('texsst.txt', 'r')
len_of_working = int(text_file.readline())
time_from_last_cleaning = int(text_file.readline())
len_of_seans = int(text_file.readline())
len_of_cleaning = int(text_file.readline())



print(count_seanses(len_of_working, time_from_last_cleaning, len_of_seans, len_of_cleaning))