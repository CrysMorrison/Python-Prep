from datetime import datetime
import sys

if(len(sys.argv)==4):
    now = datetime.now()
    f=datetime.timestamp(now)
    argumentos =str(f)+','+sys.argv[1]+','+sys.argv[2]+','+sys.argv[3]
    # argumentos = str(argumentos)
    archivo=open('clase09_ej5.csv','a+')
    archivo.write(argumentos+'\n')
    archivo.close()
    