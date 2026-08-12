def celsius_to_fahrenheit(c):
    result= round((c * 9/5) + 32, 1)
    return result
def fahrenheit_to_celsius(f):
    result= round((f - 32) * 5/9, 1)
    return result

gr=0
# celsius_to_fahrenheit(gr)
print (f'{gr}°C = {celsius_to_fahrenheit(gr)}°F')
print (f'{gr}°C = {celsius_to_fahrenheit(100)}°F')
print (f'{gr}°C = {celsius_to_fahrenheit(72)}°F')
