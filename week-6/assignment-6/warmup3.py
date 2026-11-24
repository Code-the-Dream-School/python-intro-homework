def show_message():
    message = "Hello from inside the function!"
    print(message)


show_message()

# NameError: name 'message' is not defined
# print(message)


def get_message():
    message = "Hello from the outer scope!"
    return message


outer_message = get_message()
print(outer_message)