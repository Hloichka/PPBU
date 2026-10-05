from  datetime import datetime, date, time, timedelta
####знай о разных типах данных

# d = date(2024, 12, 31)
# t = time(12, 31, 16)
# print(d, type(d))
# print(t, type(t))
# # dt = datetime.combine(d, t) ###объединяем дату и время
# # print(dt, type(dt))
# # d = date.today()
# # print(d)
# # dt = datetime.now()
# # print(dt.time())
# # dt = datetime.now().replace(microsecond=0) ###replace(microsecond=0) удаляет микросекунды
# # print(dt.time())
# # dt = datetime.now().replace(microsecond=0) ###replace(microsecond=0) удаляет микросекунды с помощью replace можно менять и день(например)
# # print(dt)
# # dt = dt.replace(year=2022, month=1, day=5)
# # print(dt)
# # dtt = input('Введите дату(дд.мм.гггг): ')
# # datte = datetime.strptime(dtt, '%d.%m.%Y')
# # print(datte)
# # print(datte.strftime('%d.%m.%Y'))
# # print(datte.strftime('%d.%m.%Y %X'))
# # print(datte.strftime('%d.%m.%Y %H:%M'))
# # print(datte.date())
# dt = datetime.now().replace(microsecond=0)
# # dtt = dt.timetuple() ####timetuple - создаст кортеж с описью - год, месяц, день, час ...
# # for i in dtt:
# #     print(i)
# dtt = dt.isocalendar() ####
# print(dtt)
# print(dt.weekday())
# print(dt.isoweekday())
# days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
# print(days[dt.weekday()]) ###вытащили индекс из переменной призваной к сег. дню

""""ввывести дату рождения"""
birthday = input('Введите дату рождения: ')

birthday = datetime.strptime(birthday, '%d.%m.%Y').date() ###перевести из строки в числовой формат
dt_now = date.today()
year_ = dt_now.year
birthday = birthday.replace(year=year_) ###какой бы год теперь не писали-мы видим дату в текущем времени
print(birthday, dt_now, year_)
if birthday < dt_now:
    birthday = birthday.replace(year=year_ + 1)
res = birthday - dt_now
if res.days == 0:
    print('С днем рождения!')
else:
    print(f'До вашего др {res.days} дней')


