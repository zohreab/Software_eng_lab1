def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2    


def root(index, radicand):
    return radicand**(1/index)

def calculator():

    print("Welcome to the Calculator app.")
    print("You can select an operation from the options listed below:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Root")


    choice = int(input("Please enter your choice number (1-6): "))

    num1 = float(input("Please enter the first number (for option 4 and 5 the first number is the base and for 6 is the index): "))
    num2 = float(input("Please enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        print(f"Result: {result}")

    elif choice == 2:
        result = subtract(num1, num2)
        print(f"Result: {result}")

    elif choice == 3:
        result = mul(num1, num2)
        print(f"Result: {result}")

    elif choice == 4:
        result = divide(num1, num2)
        print(f"Result: {result}")

    elif choice == 5:
        result = power(num1, num2)
        print(f"Result: {result}")

    elif choice == 6:
        result = root(num1, num2)
        print(f"Result: {result}")
    else:
        print("your Input is invalid!")


calculator()

