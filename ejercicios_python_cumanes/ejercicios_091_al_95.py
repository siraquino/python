# Ejercicios resueltos del 091 al 095
# Ejercicios input
#.................................................


#.................................................
# Ejercicio resuelto N091
# Problema: Solicitar por teclado nombre y apellido de una 
# persona y el programa realiza un saludo.
print()
print("-"*40)
print("Programa N091: Nombre y apellido ")
print("-"*40)

nombre = input('Introduzca su nombre: ')
apellido = input('Introduzca su apellido: ')

print('Hola '+ nombre + ' ' + apellido)

#.................................................
# Ejercicio resuelto N092
# Problema: Solictar por teclado un color
print()
print("-"*40)
print("Programa N092: Introduzca el color que te gusta")
print("-"*40)

color = input('Introduzca un color: ')

print('Te gusta el color ' + color + ' a este equipo le gusta el color de tus ojos')
print()

#.................................................
# Ejercicio resuelto N093
# Problema: Solictar por teclado una palabra
import random
print()
print("-"*40)
print("Programa N093: Introduzca una palabra")
print("-"*40)

palabra = input('Introduzca una palabra: ')
print(palabra)
print('La primera letra de tu palabra es: '+ palabra[0])
print('La última letra de tu palabra es: '+ palabra[-1])


x = len(palabra)
y = random.randint(1,x)

#print(y) quita el comentario y mira que número arroja y compara si es la letra
# Así podemos evaluar las variables y luego quitamos la linea de código
print('Una letra al azar de tu palabra es: '+ palabra[y])

#.................................................
# Ejercicio resuelto N094
# # Problema: Solictar por teclado una palabra e imprimir la inversa
print()
print("-"*40)
print("Programa N094: Inversa de una palabra")
print("-"*40)

palabra = input('Introduzca una palabra: ')
# yo practiqué con la palabra parangaricutirimicuaro
# Complementemos es estudio de: rebanadas o porciones
#  --> tarjeta (1110) y ejercicio 60
print(palabra[0:6]) # hasta el 6 sin incluirlo 
print(palabra[:6])  # hasta el 6 sin incluirlo 
print(palabra[:])   # equivale a toda la palabra
print(palabra[0:])  # equivale a toda la palabra

# practica, practica, practica

print(palabra[::]) # equivale a toda la palabra
print(palabra[0:6:2]) # desde cero hasta 6(sin incluirla, saltando 2 en 2)
# el primer : es el que ya conocemos el segundo es para saltar 
print(palabra[::-1]) # si el salto es negativo realiza la porcion desdes
# el final hasta el comienzo

print('Palabra original: ', palabra)
print('Palabra inversa: ', palabra[::-1])

#.................................................
# Ejercicio resuelto N095
# Problema: Solicitar por teclado dos numeros
print()
print("-"*40)
print("Programa N095: solicitar dos numeros")
print("-"*40)

n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número '))

print('La suma es: ', n1 + n2)
print('La multiplicación es: ', n1 * n2)



#..............................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar.
# y como estamos avanzando ahora trata de cambiar la lógica de resolución.
#
# A medida que practiquemos la creatividad se va desarrollando. La creatividad siempre ha
# estado, tan solo debemos desarrollarla, fortalecerla y ponerla a nuestra disposición.
#
# Muchos de los ejercicios los invento para desmostrar la versatilidad de python y
# como la programación dependerá de nuestra creatividad. 
#
# Rafael Aquino / julio-2020 / pythoncumanes