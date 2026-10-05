d = {
    'nama': 'alex',
    'age': 20,
    'prif': 'prog',
    'hobbis':['trevel', 'sacor', 'reading'],
    'edu':"MGU",
    'language':['russia', 'english']
}
##создание досье - список.
for k, v in d.items():
    ##проверка списов или строка?
    if isinstance(v, list):
        v = ', ' .join(v)
    print(f'{k}\t{v}')