# MANIPULATING LISTS

pets = ["Pelusa", "Gofy", "Croqueta", "Rabioso", "Perdido", "Grug"]

# Access an element

print(pets[0])

# Change an element
pets[0] = "Luigi"
print(pets)

# Print partial elements
print(pets[0:3])
# Same, 0 is default
print(pets[:3])
# Print from the latest
print(pets[-1])

# Access each certain element
print(pets[::3])
print(pets[1::2])

# Example with numbers

numbers = [range(1, 10)]
print(">>> ", numbers)
