import csv #подключем библиотеку CSV

a = input('Введите название файла (без указания расширения): ') #просим ввести название файла
exmplfile = open(a+'.csv','w',encoding='Windows-1251',newline='') #открываем файл для записи
exmplwrtr = csv.writer(exmplfile, delimiter=';') #указываем файл и разделитель в нем, в данном случае ;
exmpldt = [['ID','1','Иванов Иван Иванович'], ['ID','2','Петров Петр Петрович'], ['ID','3','Сергей Сергей Сергеевич']] #данные, которые будут записаны
#записываем данные в файл
for row in exmpldt:
    exmplwrtr.writerow(row)
exmplfile.close() #закрываем файл