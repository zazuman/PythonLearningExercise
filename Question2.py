def main():
    print("The answer to question 1:\n")
    print("The sum of the numbers above is--> " + str(sum_input_list()))

    print("\n\nThe answer to question 2:\n")
    print("The sum of the numbers above is--> " + str(sum_input_ready_list()))
    pass


# question 1
def sum_input_list():
    sum = 0
    while True:
        val = input("Enter a number or stop\n")
        if val == "stop":
            break
        try:
            int(val)
        except:
            print("Enter a number")
            continue
        sum += int(val)
    return sum


# question 2
def sum_input_ready_list():
    sum = 0
    list = input("Enter a list with ',' separating between the numbers\n")
    list.split(",")
    for i in list:
        if i != ',':
            sum += int(i)
    return sum


if __name__ == '__main__':
    main()
