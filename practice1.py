import math
from random import randint

#Work 1

a=int(input("Введите первое целое число: "))   #Первое целое число:
b=int(input("Введите второе целое число: "))   #Второе целое число:
x=int(input("Введите третье целое число: "))   #Третье целое число:

sum1= a+b+x
sum2= a*b*x

print(sum1, sum2)

#Work 2

# Координаты точек A и B
x1, y1 = 5.5, 3.5  #Координаты точки A
x2, y2 = 1.5, 2    #Координаты точки B

# Вычисление длины отрезка AB
length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
length = round(length, 3)

print("Длина отрезка AB:", length)

#Work 3

n=randint(100,1000)
print('Получено число ',n)
n = str(n)
print('Его цифры: ' + n[0] + ", " + n[1] + ", " + n[2])