def main():
    print("Enter a string")
    string = input()
    print("The new string is--> " + squeeze(string))
    pass


# func that squeezes string
def squeeze(string):
    string = str(string)
    squeezedString = ""
    countSame = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            countSame += 1
        else:
            squeezedString += string[i] + str(countSame)
            countSame = 1
    squeezedString += string[i] + str(countSame)
    return squeezedString
    pass


if __name__ == '__main__':
    main()
