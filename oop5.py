# class Car:
#     color = "yello"
#
#     @staticmethod
#     def start():
#         print("car start")
#
#     @staticmethod
#     def stop():
#         print("car stopped")
#
#
# class Toyota(Car):
#     def __init__(self, brand ):
#         self.brand = brand
#
# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type = type
#
# car1 = Fortuner("desile")
# car1.start()
# car1.color




###multi level inheritance

class A:
    varA= "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class c"

class D(C):
    varD = "welcome to class D"

class E(D):
    varE = "welcome boss "

d1 = E()
print(d1.varD)
print(d1.varC)
print(d1.varB)
print(d1.varA)
print(d1.varE)
