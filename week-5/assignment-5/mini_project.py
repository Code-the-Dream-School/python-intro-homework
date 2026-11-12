# Mini-Project: Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == "1":
        if not numbers:
            print("The list is empty.")
        else:
            min_val = numbers[0]
            for num in numbers:
                if num < min_val:
                    min_val = num
            print(f"The minimum value is {min_val}.")
            
    elif choice == "2":
        if not numbers:
            print("The list is empty.")
        else:
            max_val = numbers[0]
            for num in numbers:
                if num > max_val:
                    max_val = num
            print(f"The maximum value is {max_val}.")
            
    elif choice == "3":
        target_str = input("Enter a number to search for: ")
        if target_str.isdigit() or (target_str.startswith('-') and target_str[1:].isdigit()):
            target = int(target_str)
            found_index = -1
            for i in range(len(numbers)):
                if numbers[i] == target:
                    found_index = i
                    break
            if found_index != -1:
                print(f"Found {target} at index {found_index}.")
            else:
                print(f"{target} was not found in the list.")
        else:
            print("Invalid input. Please enter a valid integer.")
            
    elif choice == "4":
        # Make a copy so we don't permanently sort the original unless desired, 
        # or sort a working copy
        sorted_list = list(numbers)
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(sorted_list) - 1):
                if sorted_list[i] > sorted_list[i + 1]:
                    sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                    swapped = True
        print("Sorted list:")
        print(sorted_list)
        
    elif choice == "5":
        print("Goodbye! Thanks for using Number Cruncher.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
