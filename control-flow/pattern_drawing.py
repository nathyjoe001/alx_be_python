# pattern_drawing.py

def draw_square_pattern():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))
        
        # Ensure the user enters a positive integer
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Initialize the row counter
        row = 0
        
        # Use a while loop for rows
        while row < size:
            # Use a for loop for columns
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    draw_square_pattern()
