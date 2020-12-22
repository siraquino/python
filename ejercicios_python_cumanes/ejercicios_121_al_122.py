# Ejercicios resueltos del 121 al 122
# Trabajaremos con Funciones creadas por nosotros
# Return y docstring 
#.................................................
# Ejercicio resuelto N121
# Problema: crear una función que calcula la multiplicacion de 3 y 4
print()
print("-"*40)
print("Programa N121: función que calcula la multiplicacion de 3 y 4")
print("-"*40)

def multiplicacion(a,b): 
    """Función que multiplica dos números: 3 y 4"""  
    return a * b 

print("La multiplicación de 3 y 4 es: ", multiplicacion(3,4))
print("El docstring de esta función")
print(multiplicacion.__doc__)
#.................................................

# Ejercicio resuelto N122
# Problema: crear una función que suma: dos números
print()
print("-"*40)
print("Programa N122: función que suma: dos números")
print("-"*40)

def sumar(a,b): 
    """ Suma dos números introducidos por teclado"""
    return a + b

n1 =int(input("NUMERO 1: "))
n2 =int(input("NUMERO 2: "))

s = sumar(n1,n2)
print("La Suma es: ", s)


#..............................................
# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / diciembre - 2020 / pythoncumanes
