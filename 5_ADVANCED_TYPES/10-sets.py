# Set equal a group of unique values.
# Sets are unordered and unindexed.
# They are mutable, but cannot contain mutable items.

# Omit the duplicate values and print the unique values in the set.
first = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(first)

# Add and delete
# first.add(7)
# first.remove(3)
# print(first)

# Update the list with the values in the set.
second = [2, 4, 6, 8]
second = set(second)
print(second)

# Operators SETs
# print(first | second)  # Union
# print(first & second)  # Intersection
# print(first - second)  # Difference
print(first ^ second)  # Symmetric Difference

if 5 in second:
    print("5 is in the second set")
else:
    print("5 is not in the second set")
