# Ejercicios resueltos del 086 al 090
# Ejercicios Varios
#.................................................

import random

#.................................................
# Ejercicio resuelto N086
# Problema: Generar una clave especial de cuatro valores.
print()
print("-"*40)
print("Programa N086: Clave especial")
print("-"*40)

s = '#$@_*-!?'
n = '123456789'
x = random.choice(s)
y = random.choice(n)

clave = x + y 
print(clave + random.choice(s) + random.choice(n))

print("Otra forma")
x = random.choice(s)
y = random.choice(n)
clave = x + y 
x = random.choice(s)
y = random.choice(n)
clave2 = x + y 
print(clave+clave2)

#.................................................
# Ejercicio resuelto N087
# Problema: Generar un número capicua de 3 cifras
# 
print("-"*40)
print("Programa N087: Generar un número capicua de 3 cifras")
print("-"*40)

print("Primera forma")
n = random.randint(1,9)
x = n
y = n*10
z = n*100
capi = x + y + z
print(capi)

print("Segunda forma")
base = random.randint(1,9)
n = random.randint(1,9)
y = n*100
x = n
capi = y + base*10 + x
print(capi)

print()

#.................................................
# Ejercicio resuelto N088
# Problema: Lanzar un dado
# y mostrar el Resultado
print("-"*40)
print("Programa N088: Lanzar dos dados")
print("-"*40)
d1 = random.randint(1,6)
print("Dado1 lanzado = ",d1)
d2 = random.randint(1,6)
print("Dado2 lanzado = ",d2)
par = d1 ==d2 
print("El par es : ",par)

print()

#.................................................
# Ejercicio resuelto N089
# Problema: Unidad, decena y centena
# 
print()
print("-"*40)
print("Programa N089: Unidad, Decena y Centena ")
print("-"*40)

numero = random.randint(1,9)
unidad = numero
print("unidad   ", unidad)

numero = random.randint(1,9)
decena = numero*10
print("decena  ", decena)

numero = random.randint(1,9)
centena = numero*100
print("centena",centena)

print("Número ", unidad + decena + centena)

#.................................................
# Ejercicio resuelto N090
# Problema: Determinar que jugador comienza
# 
print() 
print("-"*40)
print("Programa N090: Determinar que jugador comienza")
print("-"*40)
print("~"*21)
print("| (1) Jugador rojo  | ")
print("| (2) Jugador Verde | ")
print("~"*21)
print("Corresponde jugar: (", random.randint(1,2), ")")

#..............................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar.
# y como estamos avanzando ahora trata de cambiar la lógica de resolución.
#
# A medida que practiquemos la creatividad se va desarrollando. La creatividad siempre ha
# estado, tan solo debemos desarrollarla, fortalecerla y ponerla a nuestra disposición.
#
# Muchos de los ejercicios los invento/creo para desmostrar la versatilidad de python y
# como la programación dependerá de nuestra creatividad. 
#
# Rafael Aquino / julio-2020 / pythoncumanes