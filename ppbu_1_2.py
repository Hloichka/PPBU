for math import sqrt
# PI = 3.14159

# x = 6
# n1 = int(input('Enter the value of 1:'))
# n2 = int(input('Enter the value of 2:'))
# print(n1, n2)
# print(type(n1, n2))
a = 35
b = 45
c = 55
# s = n * d / 2
# print (s)
# ''''''+, -, *, **, /, //, ''''''
p = (a * b * c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print(round(s, 2))