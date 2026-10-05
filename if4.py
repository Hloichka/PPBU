##n = int(input('Введите число: '))
##if n % 2 == 0:
##    print('Число четное')
##else:
##    print('Число не четное')
s = input('Введите время года: ')
s = s.lower()
if s == 'лето':
    print(f'{s.capitalize()} - наконец-то можно поплавать.')
elif s == 'осень':
    print(f'{s.capitalize()} - ура! Прыгать по лужам.')
elif s == 'зима':
    print(f'{s.capitalize()} - пара кататься на лыжах!')
elif s == 'весна':
    print(f'{s.capitalize()} - можно собрать одуванчики.')
else:
    print(f'{s} - это не время года!')
