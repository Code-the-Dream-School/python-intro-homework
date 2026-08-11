def celsius_to_fahrenheit(c):
    fahrenheit = round(((c * 9/5) + 32) , 1)
    print(f"{c}\xb0C = {fahrenheit}\xb0F")

def fahrenheit_to_celsius(f):
    celsius = round(((f - 32) * 5/9), 1)
    print(f"{f}\xb0F = {celsius}\xb0C")

celsius_to_fahrenheit(0)
celsius_to_fahrenheit(100)
fahrenheit_to_celsius(72)