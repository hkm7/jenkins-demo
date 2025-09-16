def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b

if __name__ == "__main__":
    # Example usage
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {add_numbers(num1, num2)}")
