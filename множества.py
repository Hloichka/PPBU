# ##1 множество
# fruits = {'apple', 'banana', 'orange'}
# ##2 много множества
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# union_set = set1.union(set2)
# print(union_set)
# ##3 пересечение множеств
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a. intersection(b)
# print(c)
# ##4 очистка множеств
# fruits = {'apple', 'banana', 'orange'}
# fruits.clear()
# print(fruits)
##5 set_1 добавление и удаление элементов.
f = {'Яблоко', 'Банан', 'Вишня'}
f2 = {'Груша', 'Апельсин', 'Манго'}
# #6 объединение списков/множества
# f3 = f.union(f2)
#7 пересечение множества f4 с множеством f2
f4 = f.intersection(f2)
# f.add('Мандарин')
# f.discard('Банан')
## print(f)
# #8 является ли ф2 подмножеством ф (типо ф2 внутри ф)
# print(f2.issubset(f))
print('Банан' in f)
