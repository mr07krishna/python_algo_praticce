# def bubbble(a):
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j]>a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# l= [3,7,1,9,2,6,3,8]
# print(bubbble(l))



#QUICK SHORT ALGORITHM

def quickshort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()

    greater = []
    lower = []
    for i in a:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return quickshort(lower) + [pivot] + quickshort(greater)

l = [3, 2, 6, 1, 8, 4, 9, 7, 5]
print(quickshort(l))
