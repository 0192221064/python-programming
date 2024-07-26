# Taking the input for the number of elements
n = int(input("Enter the number of elements:"))

# Initializing the list to store the elements
elements = []

# Taking the input for each element
for i in range(n):
    element = int(input(f"Enter the element {i + 1}:"))
    elements.append(element)

# Initializing sums for odd and even squares
odd_sum = 0
even_sum = 0

# Calculating the sum of squares for odd and even numbers
for num in elements:
    if num % 2 != 0:
        odd_sum += num**2
    else:
        even_sum += num**2

# Printing the result in the specified format
print("Sample Input:")
print("Enter the number of elements:" + str(n))
for i, el in enumerate(elements):
    print(f"Enter the element {i + 1}:" + str(el))

print("\nOutput:")
print([odd_sum, even_sum])

