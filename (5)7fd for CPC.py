import turtle as t

t.speed(3)
t.pensize(4)
t.hideturtle()

# 7 линий, все перпендикулярны горизонтальной оси (вертикальные)
lines = [
    # (x, y_start, y_end, color)
    (-180, -100, 100, 'red'),
    (-120, -100, 100, 'red'),
    (-60,  -100, 100, 'green'),    # ← зелёная
    (0,    -100, 100, 'red'),
    (60,   -100, 100, 'white'),    # ← "прозрачная" (белая на белом фоне)
    (120,  -100, 100, 'red'),
    # 7-я линия — "котёнок" (изогнутая)
]

for x, y1, y2, color in lines:
    t.penup()
    t.goto(x, y1)
    t.pendown()
    t.color(color)
    t.goto(x, y2)

# 7-я линия — в форме котёнка (силуэт)
t.penup()
t.goto(170, -100)
t.pendown()
t.color('red')

# Тело котёнка
t.setheading(90)
t.circle(30, 180)          # спинка
t.setheading(270)
t.circle(30, 180)          # животик
t.penup()
t.goto(170, 60)
t.pendown()
t.circle(20, 180)          # голова
t.penup()
t.goto(155, 75)
t.pendown()
t.dot(5, 'red')            # глазик
t.penup()
t.goto(185, 75)
t.pendown()
t.dot(5, 'red')            # глазик
t.penup()
t.goto(155, 85)
t.pendown()
t.goto(155, 100)           # ушко
t.goto(165, 90)
t.goto(175, 100)           # ушко
t.goto(175, 85)
t.goto(185, 100)           # ушко
t.goto(185, 85)

t.done()