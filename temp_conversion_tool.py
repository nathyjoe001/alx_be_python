# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # User input for temperature
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check the unit and call appropriate conversion function
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
