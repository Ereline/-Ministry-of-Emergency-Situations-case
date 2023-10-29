import os
import pandas as pd
import csv
from datetime import datetime
import datetime as dt

def nov():
    os.system("PROISh.py")
    os.system("Условия.py")

def write_data_to_csv(data):
   
    with open("data.csv", 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        csvfile.close()
        
def write_answdata(data):
   
    with open("answdata.csv", 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
        csvfile.close()        

    
def start():
    # Загрузка данных из файла CSV
    data = pd.read_csv('БАЗА.csv')
    # Вычисление количества строк в данных
    total_rows = data.shape[0]
    # Вычисление индекса, до которого нужно выводить данные (половина данных)
    half_index = total_rows // 2
    # Вывод первой половины данных
    data = data.iloc[:half_index]
    rd = {"Пожар": 5, "коммунальных": 4, "нефте": 2, "обрушение зданий": 5, "электроэнергетич": 4,"АХОВ":2, "Засуха":3, "Половодье":3, "Оползни":3, "дождевой паводок":3, "Лесные пожары":5,"кишечные инфекции людей":6,"Отравления":6, "болезни сельскохоз":6,"автодорогах":1,"Транспортные катастрофы":1,"ЖД транспорте":1,"аварии грузовых":1,"ДТП":1,"Авиационные катастрофы":1,"Загрязнения окружающей":2,"боеприпасов":5}
    
    for index, row in data.iterrows():
        D = [0,0,0,0,0,0,0,0]
        #print(row)
        pra=row[2]
        #date_str = '2023-10-27'
        """
        if pra == "21.01.1120":
            continue
        if "-" in pra:
            date_obj = datetime.strptime(pra, '%Y-%m-%d')
            """
        if "." in pra:
            date_obj = datetime.strptime(pra, '%Y.%m.%d')
            desired_format = '%Y-%m-%d'
            pra = date_obj.strftime(desired_format)
        D[0] = pra    
        
        """
        pra = pra.split("." or "-")
        print(pra)
        D[0] = datetime.date(pra[0],pra[1],pra[2])
        #date_obj = datetime.strptime(pra, '%Y-%m-%d')
        #desired_format = '%d.%m.%Y'
        #D[0] = date_obj.strftime(desired_format)
        """
        D[1]=row[0]
        a = row[1]
        for word in rd.keys():
            if word in a:
                D[rd[word]+1]=1
                write_answdata(D)
def perekat():
    D = [[],[]]
    data = pd.read_csv('answdata.csv')
    for index, row in data.iterrows():
        D[0].append(row[0])
        D[1].append(row[1])
    print("начало")
    data1 = pd.read_csv('U_DURAK.csv')
    for i in range(len(D[0])):
        lk =[0,0,0,0,0,0,0]
        a = D[0][i]
        b = D[1][i]
        #print("Виток")
        for index, row in data1.iterrows():
            pra = row[0]
            a1 = a
            b1 = pra
            if a1 < b1:
                break
            if b1==a1 and row[1].strip()==b.strip():
                for j in range(7):
                    lk[j] = row[j]
                #print(lk)
                write_data_to_csv(lk)
      

                
                
        
    
    
        
    
y = open("data.csv","w")    
y.close()
#nov()#Включить если новые данные в csv
#start()#создаёт бд answdata.csv
perekat()
