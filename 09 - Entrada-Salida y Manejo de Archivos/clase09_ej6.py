from datetime import datetime
import sys

now = datetime.now()
f= round(datetime.timestamp(now)/(60*60*24*365))
humedad= input('digite la humedad: ')
temperatura = input('digite la temperatura: ')
lluvia= input('LLovio? True/False: ')
argumentos =str(f)+','+humedad+','+temperatura+','+lluvia
archivo=open('clase09_ej6.csv','a+')
archivo.write('\n'+argumentos)
archivo.close()