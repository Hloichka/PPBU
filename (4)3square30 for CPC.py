import turtle as t
t.ht()
t.colormode(255)
t.speed(5)
t.color(0, 255, 0)
for x in [-60, 0, 60]:
    t.penup()
    t.goto(x, 0)
    t.pendown()
    for _ in range(4):
        t.fd(30)
        t.rt(90)
t.done()