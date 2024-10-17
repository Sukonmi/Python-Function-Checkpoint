#  Create four basic mathematical functions: 'add', 'subtract', 'multiply', and 'divide' that take in two numbers and return the result of the operation.

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    # Handle division by zero
    if b == 0:
        return "Error, you can't use zero"
    return a/b

# Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.

operations = {
    "+":add, 
    "-":subtract, 
    "*":multiply, 
    "/":divide
}

# Create a function 'calculator' that prompts the user to input the first number.

def calculator():
    print("Proceed to inputing your numbers")
    
    # Prompt for user to input their first number
    first_number = float(input("What is your first number: \n"))
    
    # Use a for loop to print the available operation symbols.
    print("These are the operations available")
    for symbol in operations.keys():
        print(symbol)
    
    # Create a while loop that will continue to run until the user chooses to end the current calculation.
    should_continue = True
    while should_continue:
        # Inside the while loop, prompt the user to select an operation symbol.
        user_selection = input("Select an operation or input (stop) to exit program: \n").lower()
        if user_selection == "stop":
            break
        if user_selection not in operations:
            print("Invalid operation! Try one of the following: +, -, *, /")
            continue
        
         # Prompt the user to input the second number.
        second_number = float(input("What is your second number: \n"))
        
        # Use the dictionary to retrieve the function that corresponds to the selected operation symbol and store it in a variable 'calculation_function'
        calculation_function = operations[user_selection]
        
        # Perform the calculation by calling the 'calculation_function' on the two input numbers and store the result in a variable 'answer'.
        answer = calculation_function(first_number,second_number)
        print(f"{first_number} {user_selection} {second_number} = {answer}")
        
        # Ask the user if they would like to continue using the result as the first number for further calculations.
        user_choice = input(f"Would you like to continue with {answer} as your first number? yes/no: \n").lower()

         # If the user chooses to continue, update the 'num1' variable to the value of 'answer'.
        if user_choice == "yes":
                first_number = answer

        # If the user chooses to start a new calculation, set the 'should_continue' variable to false and call the 'calculator' function to start a new calculation.
        else:
                should_continue = False
                calculator()
  
calculator()