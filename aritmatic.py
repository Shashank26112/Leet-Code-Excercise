# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Addition
addition_result = a + b
print(f"Addition: {a} + {b} = {addition_result}")

# Subtraction
subtraction_result = a - b
print(f"Subtraction: {a} - {b} = {subtraction_result}")

# Multiplication
multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")

# Division
# Checking if the second number is not zero to avoid division by zero error
if b != 0:
    division_result = a / b
    print(f"Division: {a} / {b} = {division_result}")
else:
    print("Cannot divide by zero.")

