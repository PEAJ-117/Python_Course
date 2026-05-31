numbers = [1, 12, 22, 3, 90, 4, 21, 45, 68, 77, 88, 82]

# Order with method "sort()", creating a new list
# numbers.sort()
# Order in reverse
# numbers.sort(reverse=True)
# Return a new list order with "sorted()"
numbers2 = sorted(numbers, reverse=True)

print(numbers)
print(numbers2)

# To order something complex

# users = [
#     [4, "Poled"],
#     [14, "Jhonny"],
#     [2, "Caleb"],
#     [24, "David"],
#     [5, "Ramses"]
# ]

users = [
    ["Poled", 4],
    ["Jhonny", 14],
    ["Caleb", 2],
    ["David", 24],
    ["Ramses", 5]
]

# Simple function to order by the second element of the list


# def ordena(elemento):
#     return elemento[1]

# Only anonymus function | Lambda Expression
users.sort(key=lambda el: el[1])
print(users)
