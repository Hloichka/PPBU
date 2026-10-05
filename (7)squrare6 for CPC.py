import turtle as t
t.speed(0)
t.colormode(255)
t.ht()
t.pensize(5)
for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        for d in range(4):
            t.fd(r)
            t.rt(90)
        t.end_fill()
        t.rt(60)
t.done()