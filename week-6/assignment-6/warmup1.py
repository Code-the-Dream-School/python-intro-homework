def salutation1(name):
    print("Hello, " + name + ", it's nice to meet you.")

def salutation2(name="Guest_Player"):
    if name != "Guest_Player":
        print(f"Hello, {name}! Welcome back. Would you like to continue where you left off?")
    else:
        print(f"Hello, {name}! Are you ready for a fun day with python?")

def salutation3(name, grtng):
    print(f"Hello {name}, {grtng}")

def greet_by_letter(name):
    if name[0].lower() <= "d":
        return("how are you?")
    elif "d" < name[0].lower() <= "h":
        return("What's up?")
    elif "h" < name[0].lower() <= "l":
        return("How have you been?")
    elif "l" < name[0].lower() <= "p":
        return("How's it hanging?")
    elif "p" < name[0].lower() <= "t":
        return("What's new?")
    elif "t" < name[0].lower() <= "x":
        return("What have you been up to?")
    elif "x" < name[0].lower() <= "z":
        return("How are things on your end?")

name = input("What is your name?: ")

if name == "":
    salutation2()
elif name[-1].lower() <= "i":
    salutation1(name)
elif name[-1].lower() <= "r":
    salutation2(name)
else:
    salutation3(name, greet_by_letter(name))
