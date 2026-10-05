
data = (input('Введите параметры автомобиля по шаблону\nLADA 2010г 205000км 450000руб '))
parts = data.split()
marka = parts[0]
god = parts[1]
probeg = parts[2]
cena = parts[3]
print(f'Продается автомобиль\nМарка: {marka}\nГод выпуска: {god}\nПробег: {probeg}\nЦена: {cena}')
