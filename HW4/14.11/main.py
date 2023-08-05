#   Brittany Zimmerman
#   2219602

def selection_sort_descend_trace(num):

    for i in range(len(num) - 1):
        iBig = i
        for j in range(i + 1, len(num)):
            if num[j] > num[iBig]:
                iBig = j

        tNum = num[i]
        num[i] = num[iBig]
        num[iBig] = tNum

        numL = str(num)[1:-1]
        numList = ''.join(str(numL).split(','))
        print(f'{numList} ')


if __name__ == "__main__":

    num_list = input().split(" ")
    num_list = [int(i) for i in num_list]
    selection_sort_descend_trace(num_list)
