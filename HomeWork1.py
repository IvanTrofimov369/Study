#Задание 2.1
# Два трехзначных числа
num1 = 307
num2 = 752

# Преобразование чисел в строки
num1 = str(num1)
num2 = str(num2)

# Замена средней цифры
num1new = int(num1[0] + '5' + num1[2])
num2new = int(num2[0] + '0' + num2[2])

print("Первое число с замененной средней цифрой:", num1new)
print("Второе число с замененной средней цифрой:", num2new)



#Задание 2.2

# Ввод четырехзначного числа
num = int(input("Введите четырехзначное число: "))

# Получение первой цифры
first= num // 1000
print(first)

# Получение второй цифры
second= (num // 100)%10
print(second)

# Получение третьей цифры
third= (num // 10)%10
print(third)

# Получение четвертой цифры
fourth= (num // 1)%10
print(fourth)

# Вычисление суммы первой и третьей цифры
sum= first ++ third

# Вычисление разности второй и четвертой цифры
difference= second - fourth

print("Сумма первой и третьей цифры:", sum)
print("Разность второй и четвертой цифры:", difference)


#Задание 2.3

# Ввод числа
num = int(input("Введите число: "))

# Нахождение следующего четного числа
next = num + 2 - (num % 2)

print("Следующее четное число:", next)


#Задание 2.4

#Переводим фунты в киллограммы
pounds = float(input())
kilogramm = pounds * 0.406
print(round(kilogramm, 2))

#Переводим килограммы в фунты
kilogramm = float(input())
pounds = kilogramm * 2.204
print(round(pounds, 2))