import re

a = input("Номер автомобиля: ")
b = re.compile(r'(\w{1}).*?(\d{3}).*?(\w{2}).*?(\d{2})')


if re.match(b,a):
    print("Номер верный")
else:
    print("Номер не верный")