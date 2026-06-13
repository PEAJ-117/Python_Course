# list = list([1, 2, 3])
#
# list.append(4)
# list.insert(0, 0)
#
# print(list)  # Output: [0, 1, 2, 3, 4]

class List(list):
    def prepend(self, item):
        self.insert(0, item)


list1 = List([1, 2, 3])
list1.append(4)
list1.prepend(0)
print(list1)  # Output: [0, 1, 2, 3, 4]
