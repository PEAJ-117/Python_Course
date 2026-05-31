# Multi-arguments
# def(*var)

def suma(*numbers):
    # print(a + b)
    res = 0
    for number in numbers:
        res += number
    print(res)


suma(2, 5, 6, 7, 8, 10)
suma(2, 10)
suma(2, 5, 6, 10)
suma(2)
