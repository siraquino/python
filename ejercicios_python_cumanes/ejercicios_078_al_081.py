# Ejercicios resueltos del 078 al 081
# Ejercicios Uso del módulo random
#.................................................

import random

# Ejercicio resuelto N078
# Problema: Número decimal aleatorio entre 0 y 1
print()
print("-"*40)
print("Programa N078: Número decimal aleatorio entre 0 y 1")
print("-"*40)
x = random.random()
print("El número decimal aleatorio es: ",x)
x = random.random()
print("El número decimal aleatorio es: ",x)
x = random.random()
print("El número decimal aleatorio es: ",x)
# random.random() Genera un número decimal entre 0 y 1
# puede generar el 1 pero no el cero
print()

#.................................................
# Ejercicio resuelto N079
# Problema: Generar número enteros
print("-"*40)
print("Programa N079: Generar número enteros")
print("-"*40)
x = random.randint(1,10)
print("El número entero aleatorio es: ",x)
x = random.randint(1,10)
print("El número entero aleatorio es: ",x)
x = random.randint(1,10)
print("El número entero aleatorio es: ",x)
print()

#.................................................
# Ejercicio resuelto N080
# Problema: Generar número decimales
print("-"*40)
print("Programa N080: Generar número decimales")
print("-"*40)
x = random.uniform(1,10)
print("El número entero aleatorio es: ",x)
x = random.uniform(1,10)
print("El número entero aleatorio es: ",x)
x = random.uniform(1,10)
print("El número entero aleatorio es: ",x)
print()

#.................................................
# Ejercicio resuelto N081
# Problema: seleccionar al azar un caracter de un string
print("-"*40)
print("Programa N081: Seleccionar al azar un caracter de un string")
print("-"*40)
x = random.choice('aeiou')
print("Vocal seleccionada: ",x)
x = random.choice('aeiou')
print("Vocal seleccionada: ",x)
x = random.choice('aeiou')
print("Vocal seleccionada: ",x)
print()

#..............................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar.
#
# A medida que practiquemos la creatividad se va desarrollando. La creatividad siempre ha
# estado, tan solo debemos desarrollarla, fortalecerla y ponerla a nuestra disposición.
#
# Rafael Aquino / junio-2020 / pythoncumanes