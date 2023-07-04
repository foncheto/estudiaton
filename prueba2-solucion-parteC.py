import numpy
#Crea máscara con la figura dada; 
#en teoría esto ya era parte de la prueba y no lo tenían que hacer de neuvo
mascara = numpy.ones([6,6],int)
mascara[4:,0:3]=0
mascara[3:,0:2]=0
mascara[2,0]=0
mascara[0:3,4:]=0
mascara[0:2,3:]=0
mascara[3,5]=0
print(mascara)
#Generamos una matriz de 4x4 con numeros al azar del 1 al 9 (10 sin incluir)
matriz_enteros_aleatorios = numpy.random.randint(1,10,size=(6,6))
print(matriz_enteros_aleatorios)
#multiplicamos las matrices para tener nuestro kakuro
#utilizaremos ciclos para recorrer toda la matriz
kakuro = mascara
for fila in range(0,6):
    for columna in range(0,6):
        kakuro[fila,columna] = mascara[fila,columna] * matriz_enteros_aleatorios[fila,columna]
print(kakuro)
#Sumamos filas y columnas del Kakuro
suma_filas = []
suma_columnas = []
for x in range(0,6):
    suma_filas.append(numpy.sum(kakuro[x,:]))
    suma_columnas.append(numpy.sum(kakuro[:,x]))
print(suma_filas)
print(suma_columnas)
#Generar m'ascara de n'umeros visibles
dificultad = input("Ingrese la dificultad que desea: ")
nueva_mascara = []
if dificultad == "principiante":
    #aleatorio debe mostrar 50%
    for x in range(0,18):
        aleatorio = numpy.random.random() #es un numero al azar entre 0 y 1
        if aleatorio > 0.5:
            nueva_mascara.append(1)
        else:
            nueva_mascara.append(0)
else:
    #aleatorio debe mostrar 20%
    for x in range(0,18):
        aleatorio = numpy.random.random() #es un numero al azar entre 0 y 1
        if aleatorio > 0.8:
            nueva_mascara.append(1)
        else:
            nueva_mascara.append(0)
print(nueva_mascara)
#generar tablero
