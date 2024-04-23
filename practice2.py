# Создаем пустой список для хранения введенных чисел
numbers = []

# Ввод 3 целых чисел
for i in range(3):
    num = int(input("Введите целое число: "))
    numbers.append(num)

# Находим максимальное число в списке
max1 = max(numbers)

print("Максимальное число из введенных:", max1)



# Создаем пустой список для хранения введенных чисел
numbers = []

# Ввод 5 целых чисел
#Максимальное число 5
for i in range(5):
    num = int(input("Введите целое число: "))
    numbers.append(num)

# Находим максимальное число в списке
max2 = max(numbers)

print("Максимальное число из введенных:", max2)


#Вводим последовательно возраст

age1 = int(input("Возраст Антона: "))
age2 = int(input("Возраст Бориса: "))
age3 = int(input("Возраст Виктора: "))

if age1 == age2 == age3:
    print("У всех равный возраст")
elif age1 == age2 > age3 :
    print("Антон и Борис старше Виктора")
elif age1 < age2 == age3 :
    print("Борис и Виктор старше Антона")
elif age1 > age2 < age3 :
    print("Антон и Виктор старше Бориса")
elif age1 > age2 and age1 > age3 :
    print("Антон старше всех")
elif age1 < age2 and age2 > age3 :
    print("<Борис старше всех")
elif age1 < age3 and age2 < age3 :
    print("Виктор старше всех")