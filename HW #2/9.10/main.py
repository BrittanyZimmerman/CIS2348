import csv

input1 = input()
with open(input1, 'r') as csv_file:
    word_reader = csv.reader(csv_file)

    for row in word_reader:
        word_list = list(dict.fromkeys(row))

        for word in word_list:
            count = row.count(word)
            print(word, count)
