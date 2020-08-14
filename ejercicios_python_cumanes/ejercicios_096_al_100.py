# Ejercicios resueltos del 096 al 0100
# Ejercicios input
#.................................................


#.................................................
# Ejercicio resuelto N096
# Problema: Calcular el área de un círculo
from math import pi
print()
print("-"*40)
print("Programa N096: Calcular el área de un círculo")
print("-"*40)

r = int(input('Introduzca el radio: '))

area = pi * r**2
print('El área es: ', area)

#.................................................
# Ejercicio resuelto N097
# Problema: Calcular suma de los 100 primeros números naturales
print()
print("-"*40)
print("Programa N097: suma de los 100 primeros números naturales")
print("-"*40)
# se suma 1+2+3+4...+100
s= (100*(100+1))/2
print('La suma de los 100 primeros números naturales es: ', int(s))
#otra forma
#n=100
#s= (n*(n+1))/2

#.................................................
# Ejercicio resuelto N098
# Problema: Calcular suma de los n primeros números naturales
print()
print("-"*40)
print("Programa N098: suma de los n primeros números naturales")
print("Programa N098: suma de los n primeros números naturales")
print("-"*40)
nu = int(input('Cuantos números deseas sumar: '))
# se suma 1+2+3+4...+n
su= int((nu*(nu+1))/2)
print('La suma de los',nu, ' primeros números naturales es: ', su)

#.................................................
# Ejercicio resuelto N099
# Problema: Rango de numeros aleatorios
from random import randint
print()
print("-"*40)
print("Programa N099: Rango de Números aleatorios")
print("Ejemplo Rango entre 10 y 100")
print("-"*40)

n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número mayor al primero: '))

rango = randint(n1,n2)

print('El Numero generado entre ',n1, ' y ', n2, ' es: ', rango)

#.................................................
# Ejercicio resuelto N100
# Problema: 

print()
print("-"*40)
print("Programa N0100: Mensaje")
print("-"*40)
nombre = input('Introduce tu nombre: ')
print('Felicitaciones ', nombre, 'Terminamos la primera parte del curso')

#..............................................
# Terminamos con el ejercicio 100 la primera parte de nuestro curso. 
# Esta primera parte es para aprender los rudimentos de la programación;
# tener nuestro primer contacto con un lenguaje de programación, conocer
# el shell de python y como editar los programas en un editor de texto.
#
# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / julio-2020 / pythoncumanes
