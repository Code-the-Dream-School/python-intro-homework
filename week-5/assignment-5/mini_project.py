numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    elif choice == "1":
        minimum = numbers[0]

        for number in numbers:
            if number < minimum:
                minimum = number

        print("Minimum:", minimum)

    elif choice == "2":
        maximum = numbers[0]

        for number in numbers:
            if number > maximum:
                maximum = number

        print("Maximum:", maximum)

    elif choice == "3":
        target = int(input("Enter a number to search for: "))
        found = False

        for index in range(len(numbers)):
            if numbers[index] == target:
                print("Found at index:", index)
                found = True
                break

        if found == False:
            print("Number not found.")

    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print("Sorted list:", numbers)

    else:
        print("Invalid option.")