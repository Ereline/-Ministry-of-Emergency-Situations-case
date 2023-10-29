import csv
import pandas as pd
from openpyxl import load_workbook

# def ПРОВЕРКА СуЩеСТВОВАНИЯ эксель файла база
# если нет создать и в первой строке ввести данные 
def kapec():
    global D
    df = pd.DataFrame({'Место': D[0],
                           'Тип': D[1],
                           'Дата': D[2],
                           'Время': D[3]})
    df.to_csv('БАЗА.csv',  index=False)
    
def proi():
    with open("Прои.csv", encoding='utf-8') as r_file:

        global D
        file_reader = csv.reader(r_file, delimiter = ",")
        cos = 0
        for row in file_reader:
            if cos == 0:
                cos +=1
                continue
            cos += 1
            a = row[2].split()
            row[2] = a[0]
            row.append(a[1])
            
            for i in range(4):
                D[i].append(row[i])

def ppd():
    with open("ДТП.csv", encoding='utf-8') as r_file:

        global D
        file_reader = csv.reader(r_file, delimiter = ",")
        cos = 0
        for row in file_reader:
            if cos == 0:
                cos +=1
                continue
            cos += 1
            #print(row)
            a = row[2].split()
            row[2] = a[0]
            row[3] = a[1]
            for i in range(4):
                D[i].append(row[i])

def pojar():
    with open("Пожары.csv", encoding='utf-8') as r_file:

        global D
        file_reader = csv.reader(r_file, delimiter = ",")
        cos = 0
        for row in file_reader:
            if cos == 0:
                cos +=1
                continue
            cos += 1
            #print(row)
            a = row[2].split()
            #a[0] = a[0].replace("-", "/.")
            row[2] = a[0].replace("-", ".")
            row[3] = a[1]
            for i in range(4):
                D[i].append(row[i])
    
def bam():

# Загрузите данные из файла Excel
    data = pd.read_csv("БАЗА.csv")

# Преобразуйте столбцы "Дата" и "Время" в формат datetime
   # data['Дата'] = pd.to_date(data['Дата'])
    #data['Время'] = pd.to_datetime(data['Время'], format='%H:%M:%S').dt.time

# Осуществите сортировку данных по двум столбцам "Дата" и "Время"
    sorted_data = data.sort_values(['Дата', 'Место'])

# Сохраните отсортированные данные обратно в файл Excel
    sorted_data.to_csv("БАЗА.csv", index=False)
            
#main
D = [[],[],[],[]]
proi()
ppd()
pojar()
kapec()
bam()

