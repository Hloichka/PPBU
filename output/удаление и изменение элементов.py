# t = input("введите растояние: ")
# if t.endswith("см"):
#     print("Это растояние в сантиметрах ")
# elif t.endswith("мм"):
#     print("Это растояние в миллиметрах ")
# elif t.endswith("км"):
#     print("Это растояние в киллометрах ")
# elif t.endswith("м"):
#     print("Это растояние в метрах ")
#####

# t = "Маша и Саша"
# s = t.lower()
# s1 = t.split()
# s2 = t.upper()
# s3 = t.capitalize()
# print(t)
# print(s)
# print(s1)
# print(s2)
# print(s3)

#### 1 разделение по словам
s = input("Введите ФИО:")
f, i, o = s.split()
# print(f"фамилия: {f}")
# print(f"имя: {i}")
# print(f"отчество: {o}")

#### 2 разделение слов/символос палочкой ||||
str = f"| {f} | {i} | {o} |"
print("-" * len(str))
print(str)

#### 2 разделение строк тере -------
print("-" * len(str))
print(str)



