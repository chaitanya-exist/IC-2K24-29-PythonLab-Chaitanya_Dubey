# celsius_to_fahrenheit.py
# Takes a temperature in Celsius as input, converts it to a
# number, then computes and prints the Fahrenheit value.
# Formula: F = (C * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

# Order of operations matters here: multiply/divide happen
# before the + 32 is added, so no extra parentheses are needed.
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")
