# {string:all}
point = {"x": 1, "y": 2}
print(point)
# Acccessing values
print(point["x"])
print(point["y"])

# Adding more keys
point["z"] = 35

# Key not exists
# print(point, point["oil"]) ERROR
if "oil" in point:
    print("Encontrado", point["oil"])
else:
    print("No encontrado")

# Other way to access values
print(point.get("x"))
print(point.get("oil", "No encontrado OIL"))

# Deleting a key
del point["z"]
del (point["y"])
print(point)

print("----------------------------")

# Iterating over keys
point["z"] = 35

# Returns key, value
for value in point:
    print(value, point[value])

# Returns key, value UNPACKED
for key, value in point.items():
    print(key, value)

# Returns values only
for value in point.values():
    print(value)

# Returns a tuple
for val in point.items():
    print(val)

print("----------------------------")

users = [
    {"id": 2, "name": "Jane"},
    {"id": 4, "name": "Jill"},
    {"id": 3, "name": "Jack"},
    {"id": 1, "name": "John"},
]

# for users in users:
#    print(users["name"], users["id"])

for user in users:
    print(f'ID: {user["id"]} - Name: {user["name"]}')
