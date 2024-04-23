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