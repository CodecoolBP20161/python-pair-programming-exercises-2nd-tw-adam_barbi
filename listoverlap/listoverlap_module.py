def listoverlap(list1, list2):
    for i in list1:
        if i in my_list:
            continue
        if i in list2:
            my_list.append(i)
    return (my_list)


def main():
    print(listoverlap(a, b))
    return

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_list = []

if __name__ == '__main__':
    main()
