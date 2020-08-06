# Ejercicios resueltos del 072 al 077
# Ejercicios Uso del módulo math
#.................................................

import math

# Ejercicio resuelto N072
# Problema: Usando el módulo math eliminar la parte decimal
print()
print("-"*40)
print("Programa N072: eliminar parte decimal")
print("-"*40)
cifra = 9.56
t = math.trunc(cifra)
print("Cifra original: ",cifra)
print("Cifra truncada: ",t)
print()

#.............................................
# Ejercicio resuelto N073
# Problema: Realizar la operación 2 a la 4
print("-"*40)
print("Programa N073: Operación 2 a la 4")
print("-"*40)
x = math.pow(2,4)
print("2 elevado a la 4 es: ", x)
#Si no quieres que aparezca el .0
print("2 elevado a la 4 es: ", math.trunc(x))
print()
# Otra forma (1)
# y = int(math.pow(2,4)) 
# print("2 elevado a la 4 es: ", y)
# Otra forma (2)
print()
print("2 elevado a la 4 es: ", int(math.pow(2,4)))
print()
# Importante
# puedes hacer pruebas de códigos
# colocando las líneas de código como comentarios
# prueba colocar como comentarios la 
# linea 35 y borra el # a la línea 31 y 32 
# Cualquier duda contáctame

#.............................................
# Ejercicio resuelto N074
# Problema: Realizar la operación: raiz cuadrada de 49
print("-"*40)
print("Programa N074: Realizar la operación: raiz cuadrada de 49")
print("-"*40)
z = math.sqrt(49)
print("Raiz cuadradda de 49 es: ", z)
#Si no quieres que aparezca el .0 otra forma sería
print("Raiz cuadradda de 49 es: ", int(z))
print()
# int('123') arroja 123  Ya la conocíamos 
# int(123.123) arroja 123 Otro uso

#.............................................
# Ejercicio resuelto N075
# Problema: ejercicios de redondeo hacia abajo
print("-"*40)
print("Programa N075: ejercicios de redondeo hacia abajo")
print("-"*40)
n = 49.3
r = math.floor(n)
print(n, "Redondeado hacia abajo es: ", r)
print()

#.............................................
# Ejercicio resuelto N076
# Problema: ejercicios de redondeo hacia arriba
print("-"*40)
print("Programa N076: ejercicios de redondeo hacia arriba")
print("-"*40)
n = 49.3
r_a = math.ceil(n)
print(n, "Redondeado hacia arriba es: ", r_a)
print()

#.............................................
# Ejercicio resuelto N077
# Problema: constante matemática e y pi
print("-"*40)
print("Programa N077: constante matemátca e y pi")
print("-"*40)
print("e: ", math.e)
print("PI: ", math.pi)
print()

#..............................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar.
#
# A medida que practiquemos la creatividad se va desarrollando. La creatividad siempre ha
# estado, tan solo debemos desarrollarla, fortalecerla y ponerla a nuestra disposición.
#Rafael Aquino / junio-2020 / pythoncumanes