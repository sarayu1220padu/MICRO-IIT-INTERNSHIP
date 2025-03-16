def calculator():
    # Step 1: Initialize history
    history = []
    
    # Step 2: Welcome message
    print("Welcome to the Simple Calculator!")
    print("You can perform Addition, Subtraction, Multiplication, and Division.")
    print("Enter 'history' to view Calculation history.")
    print("Enter 'clear' to clear the history.")
    print("Enter 'exit' to quit the Calculator.")
    
    while True:
        # Step 3: Get user input
        user_input = input("\nEnter an operation (+, -, *, /) or a command: ").strip().lower()
        
        # Step 4: Handle commands
        if user_input == "exit":
            print("Thank you for using the Calculator. Have a nice day!")
            break
        elif user_input == "history":
            if not history:
                print("No history available.")
            else:
                print("\nCalculation History:")
                for entry in history:
                    print(entry)
            continue
        elif user_input == "clear":
            history.clear()
            print("History cleared.")
            continue
        
        # Step 5: Validate the operation
        if user_input not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please enter +, -, *, or /.")
            continue
        
        # Step 6: Get the numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        # Step 7: Perform the calculation
        if user_input == "+":
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"
        elif user_input == "-":
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"
        elif user_input == "*":
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"
        elif user_input == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"
        
        # Step 8: Display the result and add to history
        print(f"Result: {operation}")
        history.append(operation)

# Step 9: Run the calculator
if __name__ == "__main__":
    calculator()