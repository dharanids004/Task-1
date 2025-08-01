def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", subtract(x, y))
    elif choice == '3':
        print("Result:", multiply(x, y))
    elif choice == '4':
        print("Result:", divide(x, y))
    else:
        print("Invalid choice")

    cont = input("Do you want to continue? (yes/no): ")
    if cont != 'yes':
        print("Calculator closed.")
        break
      