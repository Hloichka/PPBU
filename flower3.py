import turtle as t
t.speed(0)
t.pensize(6)
t.colormode(255)
for s in range(40, 0, -10):
    for p in range(6):
        t.color(255, 165, s * 5)
        t.fillcolor(162, s * 5, 255)
        t.begin_fill()
        t.circle(s)
        t.end_fill()
        t.rt(60)
t.done()
