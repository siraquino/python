# Programa que selecciona al azar
# una linea de un archivo existente,
# en este caso denominado: canciones.txt
# debes tener en el mismo directorio los dos archivos:
# sorteo.py y canciones.txt
import random
from random import randint
archivo = open("canciones.txt", 'r')
linea=archivo.readline()
c=0
#Mostrar y Contar el archivo de texto
titulo = "Canciones"
print(titulo.center(40, "="))
for linea in archivo:
    c=c+1
    print(linea)
print("="*40)
print("Hay :", c, "Canciones")
print("="*40)
archivo.close()
#Generar el numero aleatorio
N= random.randint(1,c)
print("Se generó aleatoriamente el número: ", N)
NN=str(N)
#Para buscar el seleccionado
archivo = open("canciones.txt", 'r')
for linea in archivo:
    seccion= linea.split(" ")
    if (NN==seccion[0]):
        print("="*40)
        print("Seleccion:  ", linea)
        print("="*40)
print("@siraquino")
print(" Fin del programa ") 