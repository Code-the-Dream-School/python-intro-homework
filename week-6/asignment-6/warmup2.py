#Write two functions:
#celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
#fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
#Call each with a few test values and print the results. Use f-strings and round to one decimal place.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Test values
celsius_values = [0, 25, 100]
fahrenheit_values = [32, 77, 212]

# Convert and print results
for c in celsius_values:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C is equal to {f:.1f}°F")

for f in fahrenheit_values:
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F is equal to {c:.1f}°C")