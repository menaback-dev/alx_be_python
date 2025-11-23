fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius():
    fahrenheit = float(input("Enter the temperature to convert: "))
    if fahrenheit != float:
        print("Invalid temperature. Please enter a numeric value.")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if unit == "f":
        result = (fahrenheit - 32) * fahrenheit_to_celsius_factor
        print(f"{fahrenheit}°F is {result}°C")
    else:
        print("Invalid unit")
convert_to_celsius()

def convert_to_fahrenheit():
    celsius = float(input("Enter the temperature to convert: "))
    if celsius != float:
        print("Invalid temperature. Please enter a numeric value.")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if unit == "c":
        result = (celsius * celsius_to_fahrenheit_factor) + 32
        print(f"{celsius}°C is {result}°F")
    else:
        print("Invalid unit")
convert_to_fahrenheit()