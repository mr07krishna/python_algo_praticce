# def show(n):
#     if (n == 3):
#         return
#     print(n)
#     show(n-1)
#
#
# show(7)


def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
p = fact(6)
print(p)