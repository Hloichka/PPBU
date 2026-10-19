# with open('ice-cream.csv', 'r', encoding='utf-8') as file:
#     ls = file.readlines()
#     for index, line in enumerate(ls):
#         pass

import math
#### открываем файл, определяем список, разделяем список на обхъекты-топинги,
#### используем только значения(убираем слова на букву Т)

result = {}
for i in open('ice-cream.csv', 'r', encoding='utf-8'):
    ls = i.strip().split(';')
    for topping in set(ls):
        if topping.startswith('t'):
            continue

            #### эти 4 строки заменили ->
        # if topping not in result:
        #     result[topping] = 1
        # else:
        #     result[topping] += 1

        #### -> этой стракой
        result[topping] = result.get(topping, 0) + 1 ### открывает наш словарь и определяет значение тобинку сколько ->
        #### -> раз взяли данный топинг?

#### способ 1 (больше занимает строк)
# mx = 0
# name_max = ''
# mn = math.inf
# name_min = ''
# for topping, count in result.items():
#     if count > mx:
#         mx = count
#         name_max = topping
#     if count < mn:
#         mn = count
#         name_min = topping

#### способ 2 (меньше занимает строк)
mx = max(result.items(), key=lambda x: x[1])[0] #### какой топинг искользуется больше всего
mn = min(result.items(), key=lambda x: x[1])[0] #### какой топинг искользуется меньше всего

# print(name_max, name_min)
print(mx, mn)