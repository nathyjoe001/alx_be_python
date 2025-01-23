# match_case_calculator.py

def match_case_calculator():
    try:
        # Prompting the user to enter the first number
        num1 = float(input("Enter the first number: "))
        
        # Prompting the user to enter the second number
        num2 = float(input("Enter the second number: "))
        
        # Prompting the user to select an operation
        operation = input("Choose the operation (+, -, *, /): ").strip()
        
        # Using match-case to determine the operation
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}")
            case "-":
                result = num1 - num2
                print(f"The result is {result}")
            case "*":
                result = num1 * num2
                print(f"The result is {result}")
            case "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}")
            case _:
                print("Invalid operation. Please choose one of +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    match_case_calculator()
