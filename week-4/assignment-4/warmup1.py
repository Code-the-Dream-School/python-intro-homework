# Hardcoded list of 8 numbers
numbers = [14, 47, 78, 3, 59, 22, 86, 40]

# 1. The first item
print(f"First:   {numbers[0]}")

# 2. The last item (using a negative index)
print(f"Last:    {numbers[-1]}")

# 3. A slice containing only the middle four items (indices 2 through 5)
print(f"Middle:  {numbers[2:6]}")

# 4. The full list in reverse order
print(f"Reversed: {numbers[::-1]}")