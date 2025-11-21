# BUILD A PYTHON CALCULATOR

print("Welcome to the Python Calculator!")
print("You will be asked to enter two numbers.")

# Step 1: Get input & convert

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

# Step 2: Perform operations

    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = None if num2 == 0 else num1 / num2

# Step 3: Display results

    print(f"\nResults:")
    print(f"{num1} + {num2} = {round(add, 2)}")
    print(f"{num1} - {num2} = {round(sub, 2)}")
    print(f"{num1} * {num2} = {round(mult, 2)}")
    
    if div is None:
        print("Division by zero is undefined.")
    else:
        print(f"{num1} / {num2} = {round(div, 2)}")

except ValueError:
    print("Please enter valid numbers.")