def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats and perform division
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        # If inputs are not numeric, catch ValueError
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any other unforeseen errors
        return f"Unexpected error: {e}"
