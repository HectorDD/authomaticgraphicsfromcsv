import csv
import numpy as np
import matplotlib.pyplot as plt


#fincas = ["San Pedro","La Ponderosa","Capellania","La estrella y Tinagua","Macanal","PAAY","MESTIZAS","PASI","Tamacara"]
fincas = ["F01","F02","F03","F04","F05","F06","F07","F08","F09"]
years = ["2014","2015","2016","2017","2018"]
def readFile(year):
    with open('Indicadores'+year+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        file={}
        for row in csv_reader:
            file[row[0]]=row[1:]
        return file

def loadIndicadores():
    f = open('listaindicadores.txt', "r")
    line = f.readline()
    indicadores=[]
    while line:
        indicadores.append(line.replace('\n',''))
        line=f.readline()
    return indicadores

def convertStrToInt(list):
    for i in range(0, len(list)): 
        if list[i]=="":
            list[i]=0
        else:
            if type(list[i]) is str:
                list[i]= float(list[i].replace(",",".")) 
            else:
                list[i]=list[i]
    return list

def getIndicador(file,name,year):
    values = convertStrToInt(file[name])
    print(values)
    plt.bar(range(9), values, edgecolor='black')
    plt.xticks(range(9), fincas, rotation=60)
    plt.title(name)
    plt.ylim(min(values), max(values)+(max(values)/10))
    #plt.show()
    plt.savefig('graficos'+year+'/'+name.replace('/','-')+'.png')
    plt.close()

def getGraphics(indicadores,year):
    file=readFile(year)
    for i in indicadores:
        getIndicador(file,i,year)

def generateGraphicsYears():
    indicadores=loadIndicadores()
    for i in years:
        getGraphics(indicadores,i)


generateGraphicsYears()

#year="2014"
#getIndicador(file,"Peso hembras a 8 meses")



