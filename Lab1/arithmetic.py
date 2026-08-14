# arithmetic.py
# Takes two numbers as input and prints their sum, difference,
# product, quotient, and remainder, each clearly labeled.

# input() always returns a string, so we convert to float
# to allow decimal numbers as well as whole numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)
