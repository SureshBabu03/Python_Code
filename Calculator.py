# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator loop
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")
    
    user = input(": ")
    
    if user == "exit":
        break
    elif user in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if user == "add":
            print("Result:", add(num1, num2))
        elif user == "subtract":
            print("Result:", subtract(num1, num2))
        elif user== "multiply":
            print("Result:", multiply(num1, num2))
        elif user == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
