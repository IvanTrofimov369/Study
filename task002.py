A=3.14
print(type(A)) #float

A='Hello'
print(type(A)) #str

a=b=c=0
a+=1 #a = a + 1
c = 5//2 #int
d = 5/2 #float
b = c**2 #b = c^2 (степень)
a, b = b, a #обмен значениями a=b, b=a

# Переменная - это величинаб имеющая имя, тип и значение. Значение переменной можно менять во время работы.

#a = input("Введите количество: ")
#print(a)

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = a+b
print(c)