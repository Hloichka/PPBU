#### пишется в той же страке в которой и применяется,
##### команда вырожается сл. образом:
#####
##### Lambda arguments: expression
##### т.е. функция агрумент: вырожение
##### multiply = lambda a, b: a * b
#####
##### наш пример
##### lbl.bind("<B1-Motion>", lambda e, c=color: globals().update(pen_color=c))
##### lbl.bind-это метка где lbl придуманно нами а bint вызывает метку к кнопке -> Button