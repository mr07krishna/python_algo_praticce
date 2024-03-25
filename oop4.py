# class person:
#     __name = "anynomues"
#
#     def __hello(self):
#         print("hello")
#
#     def welcome(self):
#         self.__hello()
#
# p1 = person()
# print(p1.welcome())


# inheritance
class Car:
    color = "yello"

    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stopped")


class Toyota(Car):
    def __init__(self, name):
        self.name = name


car1 = Toyota("fortuner")
car2 = Toyota("s clss")

print(car1.start())
print(car2.stop())
print(car2.color)
