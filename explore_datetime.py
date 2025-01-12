from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """
    Function to display the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    
    # Return the current date for further use
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    """
    Function to calculate the future date after adding user-specified days.
    """
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        # Print the future date
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Main Function
if __name__ == "__main__":
    print("Exploring Python's datetime module!")
    
    # Call the function to display the current date and time
    current_date = display_current_datetime()
    
    # Call the function to calculate the future date
    calculate_future_date(current_date)
