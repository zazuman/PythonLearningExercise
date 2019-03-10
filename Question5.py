def main():
    id = input("Input your id without the last number--> ")
    print(id + "-" + get_check_digit(id) + " is your full id")
    pass


# get last number for the id
def get_check_digit(id):
    place = 0
    sum = 0
    for num in id:
        place += 1
        if place % 2 == 1:
            sum += int(num)
        else:
            sum += deal_two_figures_result(int(num) * 2)

    return str(10 - sum % 10)
    pass


def deal_two_figures_result(num):
    if int(num) > 9:
        num = str(num)
        num = int(num[0]) + int(num[1])
    return int(num)
    pass


if __name__ == '__main__':
    main()
