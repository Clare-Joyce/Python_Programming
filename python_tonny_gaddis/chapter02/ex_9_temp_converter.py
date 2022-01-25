"""Celsius to Fahrenheit Temperature Converter.
"""

celsius_temp = float(input("Enter the temperature in celsius: "))

fahr_temp = (9/5) * celsius_temp + 32
print(f"\nFahrenheit equivalent of input: {fahr_temp}")