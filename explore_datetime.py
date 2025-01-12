from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Print the current date and time in the format "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the specified number of days
    future_date = datetime.now() + timedelta(days=days_to_add)
    
    # Print the future date in the format "YYYY-MM-DD"
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Calling the functions
display_current_datetime()
calculate_future_date()
