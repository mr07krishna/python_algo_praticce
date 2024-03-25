# # # class Car:
# # #     color = "blue"
# # #     brand = "bmw"
# # #
# # # Car1= Car()
# # # print(Car1.color)
# # # print(Car1.brand)
# #
# #
# #
# # class Student:
# #     name = "karan"
# #     def __init__(self):
# #         print(self)
# #         print("adding new student value..:-")
# #
# # s1 = Student("hari")
# # print(s1.name)
# # print(s1)
# #
#
#
# # # class Car:
# # #     color = "blue"
# # #     brand = "bmw"
# # #
# # # Car1= Car()
# # # print(Car1.color)
# # # print(Car1.brand)
# #
# #
# #
# class Student:
#     colleage_name = "ABC MORGAN"
#     name="Hello"
#     def __init__(self,name ,marks):
#         self.name = name
#         self.mark = marks
#
#         print("adding a anme in database")
#
#
# s1 = Student ("karan",20)
# print(s1.name)
# print(s1.mark)
#
# s2 = Student ("haran",40)
# print(s2.name)
# print(s2.colleage_name)
#
#
#








class student:
    colleage_name = "ABC MORGAN"
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student",self.name)

    def get_marks(self):
        return self.marks

s1= student("harii",66)
s1.welcome()
print(s1.get_marks())

