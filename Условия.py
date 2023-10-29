import csv
import pandas as pd
from openpyxl import load_workbook
import datetime as dt
def ogorod():
    global D
    with open("Данные по метеостанциям. Соответствие МО.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        cos = 0
        for row in file_reader:
            if cos == 0:
                cos +=1
                continue
            row[1] = row[1][3:]
            #print(row)
            row[0] = row[0].strip()
            if row[1] in D:
                D[row[1]].add(row[0])
            else:
                D[row[1]]={row[0]}
                
                
                
def write_data_to_csv(data):
   
    with open("U_DURAK.csv", 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        csvfile.close()

def is_numeric(value):
    try:
        float(value)  # Попытка преобразования строки в число
        return True
    except ValueError:
        return False        
        
            
    

def meteo():
    global D
    with open("Данные по метеостанциям.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        cos = 0
        L = []
        for row in file_reader:
            if cos == 0:
                cos +=1
                lk = ["Дата","Место","1","2","3","4","5"]
                write_data_to_csv(lk)
                
                continue
            a = row[0].split()
            
            #print(a)
            a1 = list(map(int,a[0].split(".")))
            a1 = dt.date(a1[2],a1[1],a1[0])
            row[0] = a1
            if L == []:
                L.append(row)
                
            elif row[0] != L[0][0]:
                alimenti = [0,0,0,0,0,0,0]
                alimenti[0] = row[0]
                for i in range(len(L)):
                    
                    if is_numeric(L[i][1]) :
                        alimenti[2]+=float(L[i][1])
                    if is_numeric(L[i][3]) :    
                        alimenti[3]+=float(L[i][3])
                    if is_numeric(L[i][5]) :
                        alimenti[4]+=float(L[i][5])
                    p = (L[i][18]).split("-")
                    if len(p) == 2:
                        alimenti[5]+=((int(p[0]))+(int(p[1])))
                    #print(p)
                    if is_numeric(L[i][22]) :
                        alimenti[6]+=float(L[i][22])
                        #print(alimenti[6])
                for ok in range(len(alimenti)-2):
                    alimenti[ok+2] = alimenti[ok+2]/(len(L))
                gor = row[29]
                if gor == "Кочево":
                    gor = "Кочёво"
                if gor == "Кын" or gor == "Усть-Черная " or gor == "Гайны":
                    continue
                if gor == "Чайковский":
                    gor = "Чайковский"
                if gor == "Октябрьский":
                    gor = "Октябрьский"
                for i in D[gor]:
                    #print(i)
                    alimenti[1] = i
                    write_data_to_csv(alimenti)
                    #print(alimenti)
                #print(alimenti)    
                L = []
                L.append(row)
            else:    
                L.append(row)
               
            
            
    
def bam():
    print("dsfd")

# Загрузите данные из файла Excel
    data = pd.read_csv("U_DURAK.csv")

# Преобразуйте столбцы "Дата" и "Время" в формат datetime
    #data['Дата'] = pd.to_date(data['Дата'])
    #data['Время'] = pd.to_datetime(data['Время'], format='%H:%M:%S').dt.time

# Осуществите сортировку данных по двум столбцам "Дата" и "Время"
    sorted_data = data.sort_values(['Дата', 'Место'])

# Сохраните отсортированные данные обратно в файл Excel
    sorted_data.to_csv("U_DURAK.csv", index=False)
            
#main
#y = open('U_DURAK.csv', "w")
#y.close()
D = {}
ogorod()
meteo()
#pojar()
#kapec()
bam()

