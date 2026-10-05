import random


##1)
# name = ['Маша', 'Марат', 'Ашот', 'Аюр', 'Снежана']
# job = ['строитель', 'доставщик', 'бареллина',
#        'школьник', 'грузчик', 'дворник', 'космонавт']
# rnd_job = random.randint(0, 6)
# rnd_name = random.randint(0, 4)
# age = random.randint(5,25)
# print(f'меня зовут: {name[rnd_name]} мне {age} лет, я {job[rnd_job]}.')

##2)
name = []
job = []
names = int(input('сколько имен введете? '))
jobs = int(input('сколько профессий введете? '))
for i in range(names):
    name.append(input('введите имя: '))
for i in range(jobs):
    job.append(input('введите профессию: '))
print(name)
print(job)
rnd_name = random.randint(0, names)
rnd_job = random.randint(0, jobs)
age = random.randint(5,25)
print(f'меня зовут: {name[rnd_name]} мне {age} лет, я {job[rnd_job]}.')

