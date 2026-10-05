# # """операция сравнения"""
# >, <, >=, <=, ==, !=
# ==
# if, not, and, or
# True and True or False ... =
# False or False(True) ... = False(True)
# a = 46
# b = 16
# c = a > b
# print (c)
#if a == b and a > b and a != b:
# if a < b or a <=b or a == b:
#    print('a < b')
#else:
#    if a > b:
#         print ("a > b")
#    elif a == b:
#    else:
#        if a < b:
#             print('a < b')
# #          else:
#            if a < b:
#             print('a < b')
#            else:
#             print('a == b')
# print('end')

#сл. операция
# h = float(input("Введите время суток: "))
# if 0 <= h < 6 or h < 0:
#     print("Morning")
# elif 12 < h < 17:
#     print("Day")
# elif h > 17 and h < 24:
#     print("Evening")
# elif h > 0 and h < 4 or h == 24:
#     print("Night")
# else:
#     print("Время введено не корректно!")

#color = input("Цвет светофора: ")
# match color:
#     case "red" | "r":
#         print("STOP")
#     case "green":
#         print("GO")
#     case "yellow":
#         print("Ready")
#     case _:
#         print("Umers", color)

#     print ("a<b")
#
# """операция сравнения"""
# """ >, <, =, ==, """
# (), not, and, or
# True and True and True(False) ... = True(Flase)
# False or False(True) ...    = False()
# ''''''
# a = 46
# b = 36
# c = a > b
# print(c)
# #
# color = input('цвет светофора: ')
# match color:
#     case 'red'| 'no':
#         print('stop')
#     case 'green':
#         print('60')
#     case 'yellow':
#         print('ready')
#     case _:
#         print('цвет', color)
"""операция сравнения"""
""">, <, >=, <=, =, ==, !="""
"""
(), not, and, or
True and True and True(False) ... = True(False)
False or False(True) ... = False(True)
"""

a = 46
b = 36
c = a > b
print(c)
z = a > b and a >= b and a == b
z1 = a < b or a <= b or a == b
print(z, z1)

# if a > b:
#     print('a > b')
# elif a < b:
#         print('a < b')
# else:
#         print('a = b')
# print('END')
#

h = float(input('Введите время суток:'))
if h >= 4 and h <= 12:
 print('morning')
elif 12 <= h <= 17:
 print('afternoon')
elif h >= 17 and h <= 24:
 print('evening')
elif h == 24 or h >= 0 and h <= 4:
 print('night')
else:
 print('Время введено не корректно')
