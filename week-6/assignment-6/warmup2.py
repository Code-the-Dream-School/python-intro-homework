def celsis_to_fahrenheit(c):
# '''converts Celsius to Fahrenheit using (c * 9/5) + 32'''
    return (c * 9/5) + 32

def fahrenheit_to_celsis(f):
# '''converts Fahrenheit to Celsius using (f - 32) * 5/9'''
    return (f - 32) * 5/9

print(f"0°C = {celsis_to_fahrenheit(0):.1f}°F")
print(f"100°C = {celsis_to_fahrenheit(100):.1f}°F")
print(f"72°F = {fahrenheit_to_celsis(72):.1f}°C")