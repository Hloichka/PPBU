# '''list'''
# import copy
# '''список - уполномоченный набор объектов'''
#
# '''  0  1  2  3  4  '''
# num = [22, 33, 44, 55, 99]
# '''  -5  -4  -3  -2  -1  '''
#
# print(num[0])
# print(num[-2])
# print(num[1:2])
# print(num[2:])
# print(num[:2])
# print(num[::2])
# print(num[::-1])
# print(num[::2])
# num = [1,2,[3,4]]
# # nn = num
# # nn = num[:]
# # nn = num.copy()
# # nn = copy.deepcopy(num)
# n = num[:]
# num[-1][1] = 400
# # print(n is num)
# print(num, id(num))
# print(n)
# print(n is num)
# x = 100
# y = 100
# # print(x is y )
# # print(id(x), id(y))
# num = [22, 33, 44, 55, 99]
#
# print(num)
# num.append(100) #добавит в конец списка 0(1) костантная (отобразиться (100) в списке)
# print(num)
# num.insert(0, 300) #0(n) линейка
# print(num)
# # num.extend([1, 2])
# print(num)
# num += [1, 2]
# # num = num + [1, 2] #чтобы рассширить список
# # print(num)
# # # num.pop() #изменяет последний элемент списка
# # print(num)
#
# n = num.pop()
# nn = num.pop(0)
# print(n, num)
# print(num)
# # while 100 in num:
# #     num.remove(100) #удаляет числа равные 100 (или той которую укажем в ()
# # print(num)
# print(num.index(100))
# print(num.count(100))
# # num.clear()
# # print(num)
# num = [22, 33, 44, 55, 99, 11]
# # for i in range(): #мне пришли цифры а мне нужна строка-конвертация выглядит так
#
# for i in range(len(num)):
#     print(num[i], end='   ') #это для того чтобы отобразить индекс с значением
# print()
#
# # ##cnt = 0 #счетчик перед цыклом
# # for i in num: #это второй способ отобразить/узнать и индекс и значение
# #     print(cnt, i, end='   ')
# #     cnt += 1
# # print()
#
# for i in enumerate(num): ##команда переводит в кортеж и выводит индекс и объект в консоль.  #способ третий - значение+индекс в скобках кортеж
#
# ##_____________________________________
# ##пример как вывести в столб-упорядочить список
# ## names = ['Dasha', 'Masha', 'Sasha', 'Glasha', 'Andryusha']
# # # names.reverse()
# # # names.sort(reverse=True)
# # names.sort()
# # for k, i in enumerate(names, 1):
# #     print(f'{k}, {i}')
# #_____________________________________
# # """ кортеж (tuple) """
# # """Кортеж - упорядоченный набор неизменяемых объектов пишится в круглых скобках"""
# ###1)упрощение списка
# # for i in range(10):
# #     ls.append(i + 1)
# # print(ls)
# # print(5 if len(ls) > 7 else 125)
# ###2)
# ###упрощение списка быстрый способ
# # ls = [i + 1 for i in range(10)]
# # print(ls)
# ### тема кортеж tuple (переносиа в другой файл)
# # tp = (22, 33, 44, 99)
# # k, *i, z = 7, 5, 9, 1, 32, 56, 100,
# # print(k, type(k), k[0])
# ##K = 7, #запятая
# ##print(K, type(K), K[0])
# # tp = (22, 33, 44, 99)
# # k, i, *z = 7, 5, 9, 1, 32, 56, 100, #распаковка
# # print(k, i, z)
# ##можно создать копию и перевести в список-изменив кортеж
# # tp = ('login', 'password')
# # print(tp, id(tp))
# # buf = list(tp)
# # buf[-1] = 'new_password'
# # tp = tuple(buf)
# # print(tp, id(tp))
#
# # '''левый циклический сдвиг''' (прокрутится в лева по одной по часовой стрелки)
# # l = [22, 33, 44, 55, 99]
# # temp = l[0]
# # n = len(l)
# # for i in range(n-1):
# #     l[i] = l[i+1]
# # l[-1] = temp
# # print(l)
# ###этот (ниже) вариант быстрее с массивами
# # temp = l.pop(0)
# # l.append(temp)
# # print(l)
#
# # x = 10
# # y = 15
# # print(x, y)
# ##классическая замена
# # z = x
# # x = y
# # y = z
# # print(x, y)
# ##питоновская замена объектов
# # x, y = y, x
# # print(x, y)
# # x, y = y, x
# # print(x, y)
#
# # while 100 in num: ## метод помогает удалить все элементы (100) (и другие значения указанные в ()) циклично т.е. все, а не одно значение.
# #     num.remove(100)
# # print(num)
#
# ## метод объединить списки имя и номер
### присвоить имени возраст+распределить по числам/строкам типо: "1. маша - 22"
names = ['Dasha', 'Masha', 'Sasha', 'Glasha', 'Andryusha']
age = [22, 33, 44, 55, 11]
for r, (n, a) in enumerate(zip(names, age), 1):
    print(f'{r}. {n} - {a}')
###переменные все типы, коллекции, циклы вайле и фор, ветвления,
###строки, списки, котеже, операторы, вложение циклов. множество, словори, функции.