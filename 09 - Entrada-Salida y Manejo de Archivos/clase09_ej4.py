import sys
if(len(sys.argv)==4):
    print('La temperatura en grados centigrados es: ', sys.argv[1])
    print('La humedad es: ', sys.argv[2])
    print('Llovio: ', sys.argv[3])
    print('los argumentos son: ', str(sys.argv))
    
else:
    print('Error . introdujo una cantidad de argumentos diferente de (3)')
    print('ejemplo: clase09.ej4.py:1 2 True')