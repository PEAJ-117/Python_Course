# Unpack List

numbers = list(range(1, 20))

first, second, *others, plast, last = numbers
print(second, plast, others)
