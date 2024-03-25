# studen = { 1 :{ 'name': 'hari','DOB': 2-2-1935, 'age': 36 },
#             2 :{ 'name': 'shya, ','DOB': 1-2-2035, 'age': 19 },
#             3 :{ 'name': 'gita ','DOB': 4-2-2945, 'age': 25 }
#         }
# print(studen.keys())
# print(studen.values())
# print(studen.items())
# print(studen.get('email','not found email element'))
# print(studen)
# # print(studen.pop('age'))
#
# for i in studen.items():
#     print(i)
#




# # #STACK DATA STRUCTURE
#
# num = []
# num.append(5)
# num.append(7)
# num.append(8)
# num.append(2)
# num.append(9)
# print(num)
# print(num.pop())
# print(num.pop())
# print(num.pop())
# print(num.pop())
# print(num.pop())
# print(num.pop())
# print(num.pop())
# print(num.pop())

def push(num, n):
    num.append(n)

def pop(num):
    if isEmpty(num):
        print("Stack is empty")
    else:
        return num.pop()

def isEmpty(num):
    return not num

num = []
push(num, 5)
push(num, 7)
push(num, 8)
push(num, 2)
push(num, 9)
print(num)
print(pop(num))
print(pop(num))
print(pop(num))
print(pop(num))
print(pop(num))  # This will print "Stack is empty"
print(pop(num))




