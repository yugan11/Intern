numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))  # Square each number
cubes = list(map(lambda x: x**3, numbers))    # Cube each number
print("Original numbers:", numbers)
print("Squared numbers:", squares)
print("Cubed numbers:", cubes)
