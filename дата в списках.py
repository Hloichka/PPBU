import datetime
t = datetime.date.today()
ru = ''
# date = t.strftime("%d %B %Y")
m = t.month #храним номер месяца в m
s = ['января', 'февраля', 'марта', 'апреля',
     'мая', 'июня', 'июля', 'августа','сентября',
     'октября', 'ноября', 'декабря']
month_ru = s[m -1]
print(f'сегодня: {t.day} {month_ru} {t.year} года.')