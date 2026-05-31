# Tupla = List inmutable

numbers = (1, 2, 3, 4, 5) + (6, 7, 8, 9, 10)
print(numbers)

point = tuple([1, 2])
print(point)
lessNumber = numbers[:2]
print(lessNumber)

prime, second, *others = numbers
print(prime, second, others)
for n in numbers:
    print(n)

listNumbers = list(numbers)
listNumbers[0] = "Hellow"
print(listNumbers)

# Modify the list, no a tupla
