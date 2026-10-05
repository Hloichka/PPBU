import datetime

# t = datetime.datetime.now()
# print(f' : {t}')

# t = datetime.date.today()
# date = t.strftime("%d %B %Y")

t = datetime.date.today()
ru = ''
# date = t.strftime("%d %B %Y")
m = t.month #храним номер месяца в m
# print(f' : {m}')
if m == 1:
    ru = 'января'
if m == 2:
    ru = 'февраля'
if m == 3:
    ru = 'марта'
if m == 4:
    ru = 'апреля'
if m == 5:
    ru = 'мая'
if m == 6:
    ru = 'июня'
if m == 7:
    ru = 'июля'
if m == 8:
    ru = 'августа'
if m == 9:
    ru = 'сентября'
if m == 10:
    ru = 'октября'
if m == 11:
    ru = 'ноября'
if m == 12:
    ru = 'декабря'
print(f'сегодня: {t.day} {ru}  {t.year} года.')