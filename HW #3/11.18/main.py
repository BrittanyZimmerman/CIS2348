
user_inp = input()
number_list = []

for i in user_inp.split():
    number_list.append(int(i))
    temp = int(i)
    if temp < 0:
        number_list.pop()

number_list.sort()

for i in number_list:
    print(i, end=' ')






