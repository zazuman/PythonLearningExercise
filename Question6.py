def main():
    list = [1, 2, 3, 4, 5, 6]
    print(list)
    list = map(list, add5)
    print(list)
    pass


def map(list, func):
    for i in range(len(list)):
        list[i] = func(list[i])
    return list
    pass


# func that changes the info in the list in map func
def add5(num):
    return num + 5
    pass


if __name__ == '__main__':
    main()
