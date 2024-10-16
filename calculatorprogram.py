#  Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

# Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.

operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

# Create a function 'calculator' that prompts the user to input the first number.

def calculator():
    print("Proceed to inputing your numbers")
    # Prompt for user to input two numbers
    first_number = int(input("What is your first number: \n"))
    second_number = int(input("What is your second number: \n"))
    # Use a for loop to print the available operation symbols.
    print("These are the operations available")
    for symbol in operations.keys():
        print(symbol)
    # Create a while loop that will continue to run until the user chooses to end the current calculation.
    while True:
        # Inside the while loop, prompt the user to select an operation symbol.
        user_selection = input("Select an operation or input (stop) to exit program: \n").lower()
        # Use the dictionary to retrieve the function that corresponds to the selected operation symbol and store it in a variable 'calculation_function'
        # Perform the calculation by calling the 'calculation_function' on the two input numbers and store the result in a variable 'answer'.
        if user_selection == "stop":
            break
        if user_selection == "+":
            calculation_function = operations["+"]
            result = add(first_number,second_number)
            print(f"{first_number}+{second_number} = {result}")
        elif user_selection == "-":
            calculation_function = operations["-"]
            result = subtract(first_number,second_number)
            print(f"{first_number}-{second_number} = {result}")
        elif user_selection == "*":
            calculation_function = operations["*"]
            result = multiply(first_number,second_number)
            print(f"{first_number}*{second_number} = {result}")
        elif user_selection == "/":
            calculation_function = operations["/"]
            result = divide(first_number,second_number)
            print(f"{first_number}/{second_number} = {result}")
        else:
            print("This operation is not available. Try any of the following(+,-,*,/)")
    # Ask the user if they would like to continue using the result as the first number for further calculations.

calculator()