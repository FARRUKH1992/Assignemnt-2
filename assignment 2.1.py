# Task 1 and 2: Determine the Smallest and Greatest Numbers
# Identify largest of three numbers
# Identify smallest of three numbers
# Prompt the user to enter three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
largest = max(num1, num2, num3)

# Find the smallest number
smallest = min(num1, num2, num3)

# Print the results
print(f"The smallest number is {smallest}. The largest number is {largest}.")