numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum

def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum

def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1

def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(len(sorted_numbers) - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]

    return sorted_numbers

def show_menu():
    print("\n=== Number Cruncher ===")
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
            print("Minimum:", find_min(numbers))

        elif choice == "2":
            print("Maximum:", find_max(numbers))

        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            result = search(numbers, target)

            if result != -1:
                print(f"Found at index {result}.")
            else:
                print("Number not found.")

        elif choice == "4":
            print("Sorted list:", bubble_sort(numbers))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()