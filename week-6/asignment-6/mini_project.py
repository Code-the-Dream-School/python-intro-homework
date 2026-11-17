numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
#Define the following functions, each taking numbers (a list) as a parameter:
#find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

#find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

#search(numbers, target) — returns the index of target, or -1 if not found
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

#bubble_sort(numbers) — returns a new sorted list (do not modify the original)
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
                swapped = True
        if not swapped:
            break
    return sorted_numbers

#show_menu() — prints the menu options and returns the user's choice as a string
def show_menu():
    print("\n======Menu:======")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Sort the List")
    print("5. Quit")
    choice = input("Enter your choice: ")
    return choice

#main() — the while loop that calls show_menu() and dispatches to the right function
def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print(f"Minimum value: {find_min(numbers)}")
        elif choice == "2":
            print(f"Maximum value: {find_max(numbers)}")
        elif choice == "3":
            target = int(input("Enter the number to search for: "))
            index = search(numbers, target)
            if index != -1:
                print(f"Number found at index: {index}")
            else:
                print("Number not found.")
        elif choice == "4":
            sorted_list = bubble_sort(numbers)
            print(f"Sorted list: {sorted_list}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

#Call main() at the bottom of the file.
main()