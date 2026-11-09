numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    '''return the smallest number in the list'''
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def find_max(numbers):
    '''returnts the largest number in the list'''
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest  

def search(numbers, target):
    '''return the index of the target number or -1 if not found'''
    for i in range (len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    '''sort the numbers from smallest to largest'''
    #do not use the original list
    my_list = numbers.copy()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
    return my_list    

def show_menu():
    #user selects an option
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")
    return choice 

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            smallest = find_min(numbers)
            print("The smallest number is:", smallest)

        elif choice == "2":
            largest = find_max(numbers)
            print("The largest number is:", largest)

        elif choice == "3":
            target = input("Type the number you're searching for: ")
            if target.isdigit():
                index = search(numbers, int(target))
                if index == -1:
                    print("Not Found")
                else:
                    print(f"Found at index {index}") 
            else:
                print("Please enter a whole number.")           

        elif choice == "4":
            my_list = bubble_sort(numbers)
            print("Sorted list:", my_list)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("That is an invalid option. Please enter a number 1-5. ")

  
main()      

            

