# это программа рисует круги
# print(range(2, 5))


import turtle as t
Ugol = 7
t.color('red')
t.begin_fill()
for i in range(Ugol):
    t.fd(80)
    t.right(360 * 3 / Ugol)
t.end_fill()