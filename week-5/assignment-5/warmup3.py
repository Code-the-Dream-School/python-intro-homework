names=['Sara','Mike','Sophie','Luke']
name=input("Enter a name to search for: ")
index=0
flag =0
for n in names:
    index += 1
    if n.lower() ==  name.lower():
       print(f"Found {n} at index {index-1}.")
       flag=1

if flag==0:    
    print(f"{name} was not found in the list.")
