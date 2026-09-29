def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))


if __name__ == "__main__":
    main()
