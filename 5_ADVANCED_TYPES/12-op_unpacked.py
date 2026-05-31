# list = [1, 2, 3, 4, 5]
# list = (1, 2, 3, 4, 5)
# print(1, 2, 3, 4, 5)
# print(*list)  # unpacking the list
#
# list2 = [6, 7, 8, 9, 10]
#
# unpacking both lists into a new list
# combined = ["Hellow", *list, "World", *list2, "PEAJ"]
# print(combined)

point1 = {"x": 12, "y": 2}
point2 = {"y": 22}
newPoint = {**point1, "Beach": "Great", **point2, "z": 0}
# unpacking the dictionaries, if there are duplicate keys, the last one will be used
print(newPoint)
