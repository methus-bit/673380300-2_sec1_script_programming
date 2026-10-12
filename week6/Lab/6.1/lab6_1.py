# lab6_1.py - Simple Calculator Functions

def add(a, b):
    """Adds two numbers and returns their sum."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the result. 
    Handles division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base, exponent=2):
    """Calculates the power of a base to an exponent. 
    Default exponent is 2 for squaring if not provided."""
    return base ** exponent

def main():
    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (Base ^ Exponent)")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")
        
        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                if choice != '5':
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                exp_input = input("Enter exponent (leave blank to use default 2): ")
                if exp_input.strip() == "":
                    print(f"Result: {power(num1)}")
                else:
                    try:
                        exp = float(exp_input)
                        print(f"Result: {power(num1, exp)}")
                    except ValueError:
                        print("Invalid exponent. Using default 2.")
                        print(f"Result: {power(num1)}")
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()