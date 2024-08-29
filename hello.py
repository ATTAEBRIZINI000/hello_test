def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial_recursive(number)}")
