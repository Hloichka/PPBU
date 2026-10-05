# import turtle as t
# t.ht()
# r = 40
# t.pensize(5)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for j in range(4):
#     for _ in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r = r - 10
# t.done()
# import turtle as t
# t.speed(0)
# t.ht()
# r = 20
# t.pensize(4)
# t.color("#FFA500")
# t.fillcolor("#A200FF")
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(r)
#         t.end_fill()
#         t.rt(60)
#     r = r - 5
# # d = 20
# t.penup()
# t.fd(80)
# t.pendown()
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(d)
#         t.end_fill()
#         t.rt(60)
#     d = d - 5
# k = 20
# t.penup()
# t.fd(80)
# t.pendown()
# for j in range(4):
#     for i in range(6):
#         t.begin_fill()
#         t.circle(k)
#         t.end_fill()
#         t.rt(60)
# #     k = k - 5
# t.done()
import turtle as t
t.speed(0)
t.ht()
r = 20
t.pensize(4)
t.color("#FFA500")
t.fillcolor("#A200FF")
for s in range(3):
    for j in range(4):
        for i in range(6):
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
        r = r - 5
    t.penup()
    t.fd(80)
    t.pendown()
    r = 20

