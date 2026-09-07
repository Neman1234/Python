def addition(a , b):
    return a + b

def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b

def division (a, b):
    if b == 0:
        return "Error : Divisor cannot be zero"
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_choice():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return input("Enter choice (1-5): ")


def calculate(choice, a, b):
    if choice == "1":
        return addition(a, b)
    elif choice == "2":
        return subtraction(a, b)
    elif choice == "3":
        return multiplication(a, b)
    elif choice == "4":
        return division(a, b)
    else:
        return "Error: Invalid choice"


def main():
    print("=== Simple Calculator ===")
    while True:
        choice = get_choice()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-5.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        result = calculate(choice, a, b)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()