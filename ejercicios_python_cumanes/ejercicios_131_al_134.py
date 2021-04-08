# Ejercicios resueltos del 131 al 134
# Ejercicios de Valor Absoluto y Opuestos

#.................................................
# Ejercicio resuelto N131
# Problema: Calcular el Valor absoluto de un número sin usar abs(x)
print()
print("-"*40)
print("Programa N131: Calcular el Valor absoluto de un número")
print("-"*40)

n = int(input('Introduzca el número: '))

if n >= 0:
    print ("El valor absoluto de ", n, "es: ",n)
else:
    print ("El valor absoluto de ", n, "es: ",-1*n)
    print ("El valor absoluto de ", n, "es: ",((n*-2) -(-n)))

# Revisa el ejercicio 101 (Valor absoluto) 
# Se me ocurrio también: Con lapiz y papel! esto ((n*-2) -(-n)))
# print ("El valor absoluto de ", n, "es: ",((n*-2) -(-n)))
# revísalo a ver si funciona! / intenta otra forma!
#.................................................


# Ejercicio resuelto N132
# Problema: Calcular el opuesto de un número
print()
print("-"*40)
print("Programa N132: Calcular el Opuesto de un número")
print("-"*40)

n = int(input('Introduzca el número: '))

print("El Opuesto es: ", -1*n)
Intenta hacerlo usando abs(n)
#.................................................

# Ejercicio resuelto N133
# Problema: Verificar si dos números tienen el mismo valor absoluto
print()
print("-"*40)
print("Programa N133: Verificar si dos números tienen el mismo valor absoluto")
print("-"*40)

n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el segundo número: '))

if (abs(n1) == abs(n2)):
    print ('Si tienen el mismo valor absoluto')
else:
    print ('No tienen el mismo valor absoluto')
#.................................................

# Ejercicio resuelto N134
# Problema: Verificar que dos números son opuesto
print()
print("-"*40)
print("Programa N134: Verificar si dos números son opuestos")
print("-"*40)

n1 = int(input('Introduzca el primer número: '))
n2 = int(input('Introduzca el el opuesto del número anterior: '))

if (abs(n1) == abs(n2)) and (n1 != n2):
    print ('Si son opuestos')
else:
    print ('No son opuestos')

# Otra forma
# Supongamos que n1 = 1 y n2 = -1 (son opuestos)
# Debo realizar una operación que me de 0 para que sean opuestos 
# inténtalo o si consigues otra forma! 

# Puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / febrero - 2021 / pythoncumanes