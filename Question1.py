# declaring important variable
balance = 100000
code = '123456'


def check_code(entered_code):
    # checking if correct code
    global code
    if entered_code == code:
        return True
    else:
        return False


def update_code():
    # checking if number
    global code
    newCode = input("\nEnter the new secret code\n")
    while not newCode.isdigit():
        newCode = input("\nThat's not a number!\n")
    code = newCode


def withdrawal_money_from_account():
    print("Enter 1 for getting 20 dollar from the account\n"
          "Enter 2 for getting 50 dollar from the account\n"
          "Enter 3 for getting different amount of money from the account\n")
    option = input()
    while not option.isdigit():
        option = input("\nThat's not a number!\n")
    while True:
        if option == '1':
            get_money(20)
            break
        if option == '2':
            get_money(50)
            break
        if option == '3':
            amount = input("Enter the amount of money you want to withdrawal\n")
            try:
                int(option)
            except ValueError:
                print("That's not a number!")
                continue
            get_money(int(amount))
            break
        print("Enter a number between 1-3")


def get_money(amount):
    # updating the balance
    global balance
    balance = balance - int(amount)


while True:
    enteredCode = input("Enter your secret code\n")
    # checking if number
    try:
        val = int(enteredCode)
    except ValueError:
        print("That's not a number!")
        continue
    # checking if correct code
    if not check_code(enteredCode):
        print("Invalid code. Try again")
        continue

    print("\nEnter 1 for printing current balance"
          "\nEnter 2 for pulling money from the account"
          "\nEnter 3 for changing the secret code"
          "\nEnter 4 for exit")
    instruction = input()
    # dealing with each case:

    # in case of printing balance
    if instruction == '1':
        print(balance)
        continue
    # in case of withdrawing money
    if instruction == '2':
        withdrawal_money_from_account()
        continue
    # in case of updating secret code
    if instruction == '3':
        update_code()
        continue
    # in case of exiting the ATM
    if instruction == '4':
        break
print("pleasure doing business with you :D")
