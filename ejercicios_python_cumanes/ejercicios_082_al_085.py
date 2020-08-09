# Ejercicios resueltos del 082 al 085
# Ejercicios Varios
#.................................................

import random

#.................................................
# Ejercicio resuelto N082
# Problema: Realizar la tabla de multiplicar al azar.
# Primera Forma   
print()
print("-"*40)
print("Programa N082: tabla de multiplicar al azar")
print("-"*40)
n = random.randint(1,10)
s = '123456789' 
print("Tabla de multiplicar del: ", n)
x = int(s[0])
print(n, " * ",x , " = ", n*x)
x = int(s[1])
print(n, " * ", x, " = ", n*x)
x = int(s[2])
print(n, " * ", x, " = ", n*x)
x = int(s[3])
print(n, " * ", x, " = ", n*x)
x = int(s[4])
print(n, " * ", x, " = ", n*x)
x = int(s[5])
print(n, " * ", x, " = ", n*x)
x = int(s[6])
print(n, " * ", x, " = ", n*x)
x = int(s[7])
print(n, " * ", x, " = ", n*x)
x = int(s[8])
print(n, " * ", x, " = ", n*x)
print()


#.................................................
# Ejercicio resuelto N083
# Problema: Se desea saber el número ganador
# de una rifa de 100 números
print("-"*40)
print("Programa N083: Rifa")
print("-"*40)

x = random.randint(1,100)
print("Número ganador: ",x)

print()

#.................................................
# Ejercicio resuelto N084
# Problema: Lanzar un dado
# y mostrar el Resultado
print("-"*40)
print("Programa N084: Lanzar dados")
print("-"*40)
x = random.randint(1,6)
print("Número: ",x)

print()



# Ejercicio resuelto N085
# Problema: Comparar el número 10 con un
# un número aleatorio del 1 al 20
print()
#Encabezado INICIO
print("-"*40)
print("Programa N085: Comparación ")
print("-"*40)

# Datos de Entrada
numero = 10
aleatorio = random.randint(1,20)

# Procesos....................
print("Verificar si", numero, "es > que ", aleatorio)
comparo = numero > aleatorio
print("El Resultado es: ", comparo)
print()

print("Verificar si", numero, "es >= que ", aleatorio)
comparo = numero >= aleatorio
print("El Resultado es: ", comparo)
print()

print("Verificar si", numero, "es < que ", aleatorio)
comparo = numero < aleatorio
print("El Resultado es: ", comparo)
print()

print("Verificar si", numero, "es <= que ", aleatorio)
comparo = numero <= aleatorio
print("El Resultado es: ", comparo)
print()

print("Verificar si", numero, "es Diferente a", aleatorio)
comparo = numero != aleatorio
print("El Resultado es: ", comparo)
print()

print("Verificar si", numero, "es igual a", aleatorio)
comparo = numero == aleatorio
print("El Resultado es: ", comparo)
# Fin de Procesos................
# Hay 6 procesos y notamos que todos tienen similitud
# al tipearlos. Podemos tipear el primero y copiar y
# pegar los demás, modificando lo que aplique.
print()

#..............................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar.
#
# A medida que practiquemos la creatividad se va desarrollando. La creatividad siempre ha
# estado, tan solo debemos desarrollarla, fortalecerla y ponerla a nuestra disposición.
#
# Rafael Aquino / julio-2020 / pythoncumanes