def cel2fah(celsius):
  #converts cel 2 fah
  fahrenheit = (celsius * 9/5) + 32
  #round
  return f"{celsius} Celsius is {round(fahrenheit, 1)} Fahrenheit"

print(cel2fah(26))
print(cel2fah(30))
print("====================")

def fah2cel(fahrenheit):
  #converts fah 2 cel
  celsius = (fahrenheit - 32) * 5/9
  #round
  return f"{fahrenheit} Fahrenheit is {round(celsius, 1)} Celsius"

print(fah2cel(26))
print(fah2cel(30))