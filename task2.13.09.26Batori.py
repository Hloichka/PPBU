##
##password = ""
##while password != range(8-20):
##    password = input('Введите пароль: ')
##    print('Пароль подходит.')
##    
##    if password = 8
##        print('Пароль введен не верно. Попробуйте еще раз. ')
##    
##
##
##k = input('Введите пароль')
##while 8 <= k <= 20:
##    print('Пароль подходит. Сохранить пароль?')
##
##    k +=8
##
##while True:
##    k = input('Введите пароль')
##    if 8 <= k <= 20:
##        print('Пароль актуален. ')
##        break
##    else:
##        print('Пароль не корректен')


n = (input('Введите пароль: '))
while len(n) < 8:
    print('Минимум 8 символов. ')
    n = (input('Введите снова: '))
    print(n)
##    break
else:
    print('Пароль принят. ')


