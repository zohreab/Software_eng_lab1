def calculator():

    print("Welcome to the Calculator app.")
    print("You can select an operation from the options listed below:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("3. Divide")
    print("5. Power")
    print("6. Root")


    choice = int(input("Please enter your choice number (1-6): "))

    num1 = input("Please enter the first number (for choices from 4 to 6 the first number is the base): ")
    num2 = input("Please enter the second number: ")

    if choice == 1:
        Add(num1, num2)
    elif choice == 2:
        Sub(num1, num2)
    elif choice == 3:
        Mul(num1, num2)
    elif choice == 4:
        Div(num1, num2)
    elif choice == 5:
        Power(num1, num2)
    elif choice == 6:
        Root(num1, num2)
    else:
        print("your Input is invalid!")


calculator()

