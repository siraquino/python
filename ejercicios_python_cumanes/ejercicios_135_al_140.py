# Ejercicios resueltos del 135 al 140
# Ejercicios de FOR (para)

#.................................................
# Ejercicio resuelto N135
# Problema: Visualizar por pantalla los números del 1 al 5
print()
print("-"*40)
print("Programa N135: Visualizar por pantalla los números del 1 al 5")
print("-"*40)

for i in range(1,6):
    print(i, end=" ")
# Revisa los ejercicios N065 al N069
# Con el uso del "for" mejoramos nuestro código

#.................................................

# Ejercicio resuelto N136
# Problema: Tabla de multiplicar del 9
print()
print("-"*40)
print("Programa N136: Tabla de multiplicar del 9")
print("-"*40)
print("Tabla de Multiplicar del 9")

for i in range(1,11):
    print( 9, " * ",i , " = ", 9 * i )
#Revisa el ejercicio N70


#.................................................

# Ejercicio resuelto N137
# Problema: Tabla equivalencia del Bolívar y Dollar.
print()
print("-"*40)
print("Tabla de conversión")
print("-"*40)
dollar = 1000000
print("Valor del Dollar: ", dollar)
print("$     Bolívares")
for i in range(1,11):
    print(i, " = ", dollar*i)
#Revisa el ejercicio N71

#.................................................
# Ejercicio resuelto N138
# Problema: Realizar la Tabla de multiplicar al azar.
 
print()
print("-"*40)
print("Programa N138: tabla de multiplicar al azar")
print("-"*40)
import random
n = random.randint(1,10)
print("Tabla de multiplicar del: ", n)
    
for i in range(1,11):
    print(i, " * ",n , " = ", n*i)
    #Revisa el ejercicio N82

#.................................................
# Ejercicio resuelto N139
# Problema: Realizar la tabla de multiplicar de un 
# número solicitado por teclado   
print()
print("-"*40)
print("Programa N139: Tabla de multiplicar")
print("-"*40)

numero = int(input("Cual tabla de multiplicar deseas visualizar: "))
print("Tabla de multiplicar del: ", numero)
    
for i in range(1,11):
    print(i, " * ",numero , " = ", numero*i)
print()
#.................................................
# Ejercicio resuelto N140
# Problema: Generar 10 numeros enteros aleatorios
print()
print("-"*40)
print("Programa N140: Generar 10 numeros enteros aleatorios")
print("-"*40)

import random
for i in range(1,11):
    print(random.randint(1,10),end= "  ")

# Revisar ejercicio N79

#.................................................
# Ejercicio Extra!
# Escribir el siguiente código y visualizar el resulatado
print()
print("-"*40)
print("ejercicio Extra!")
print("-"*40)
for i in range(1,21):
    print("*"*i)

# Ejercicio parecido al N56


####################################################
# Puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / febrero - 2021 / pythoncumanes