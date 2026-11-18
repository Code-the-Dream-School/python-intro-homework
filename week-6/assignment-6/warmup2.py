def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"32°F = {fahrenheit_to_celsius(32):.1f}°C")
print(f"86°F = {fahrenheit_to_celsius(86):.1f}°C")