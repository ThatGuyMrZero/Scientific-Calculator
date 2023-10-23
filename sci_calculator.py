import math

sum_of_calculation = 0.0
num_calculations = 0
previous_result = 0.0
display_menu = True


def get_operand(prompt):
    operand = input(prompt + ": ")
    if operand == "RESULT":
        operand = previous_result
    else:
        operand = float(operand)
    return operand


def addition():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    print()
    result = first_operand + second_operand
    return result


def subtraction():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    result = first_operand - second_operand
    return result


def multiplication():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    result = first_operand * second_operand
    return result


def division():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    result = first_operand / second_operand
    return result


def exponentiation():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    result = math.pow(first_operand, second_operand)
    return result


def logarithm():
    first_operand = get_operand("Enter first operand ")
    print()
    second_operand = get_operand("Enter second operand ")
    result = math.log(second_operand, first_operand)
    return result


def average():
    if num_calculations == 0:
        print("Error: No calculations yet to average!")
    else:
        average_result = sum_of_calculation / num_calculations
        print(f"Sum of calculations: {sum_of_calculation}")
        print(f"Number of calculations: {num_calculations}")
        print(f"Average of calculations: {average_result: .2f}")


result = float(0.0)
print(f"Current Result: {result}")
print()

while True:
    if display_menu:
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")
        print()

    choice = int(input("Enter Menu Selection: "))
    print()

    if choice == 0:
        print("Thanks for using this calculator. Goodbye!")
        break
    elif choice in [1, 2, 3, 4, 5, 6]:
        result = 0.0
        if choice == 1:
            result = addition()
            print(f"Current Result: {result}")
            print()
        elif choice == 2:
            result = subtraction()
            print(f"Current Result: {result}")
            print()
        elif choice == 3:
            result = multiplication()
            print(f"Current Result: {result}")
            print()
        elif choice == 4:
            result = division()
            print(f"Current Result: {result}")
            print()
        elif choice == 5:
            result = exponentiation()
            print(f"Current Result: {result}")
            print()
        elif choice == 6:
            result = logarithm()
            print(f"Current Result: {result}")
            print()
        sum_of_calculation += result
        num_calculations += 1
        previous_result = result
    elif choice == 7:
        if num_calculations == 0:
            print("Error: No calculations yet to average!")
        else:
            average()
        display_menu = False
    else:
        print("Error: Invalid selection!")
        display_menu = False
