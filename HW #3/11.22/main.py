
word_list = input()
words = word_list.split()


for i in words:
    count = words.count(i)
    print(i, count)
