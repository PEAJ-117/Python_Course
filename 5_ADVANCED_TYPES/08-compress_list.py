users = [["Alice", 30], ["Bob", 2], ["Charlie", 5]]

# names = []
# for user in users:
#     names.append(user[0])
# print(names)

# Transforming the above code into a list comprehension
# names = [user[0] for user in users]
# print(names)

# Flitering and transforms the list using a condition
# names = [user for user in users if user[1] > 2]
# print(names)

# Map & Filter
# names = list(map(lambda user: user[0, users]))

lessUser = list(filter(lambda user: user[1] > 2, users))
print(lessUser)
