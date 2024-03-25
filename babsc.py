# email = input("email")
# password = input("password")
# if email == "xyz@gmail.com" and password == "12345":
#     print("welcome")
# else:
#     print("incorrect")





#####EMAIL@ @@@ @@@@@ VALIDATIONS

# email = input("email")
# password = input("password")
#     if email == "asd@gmail.com" and password == "123":
#         print("welcome")
#     elif email == "asd@gmail.com" and password != "123":
#         print("incorrect password")
#         password = input("re-type password")
#         if password =="123":
#             print("welcome")
#         else:
#             print("still incorrect")
# else:
#     print("incorrect")



email = input("email:-")
if '@' in email:
    password = input("password:-")
    if email == "asd@gmail.com" and password == "123":
        print("welcome")
    elif email == "asd@gmail.com" and password != "123":
        print("incorrect password")
        password = input("re-type password")
        if password =="123":
            print("welcome ")
        else:
            print("still incorrect")
    else:
        print("incorrect")
else:
    print("incorrect email type")