# Ejercicios resueltos del 111 al 114
# Trabajaremos con Funciones creadas por nosotros 
#.................................................
# Ejercicio resuelto N111
# Problema: .
print()
print("-"*40)
print("Programa N111: crear una función que muestre un saludo")
print("-"*40)

#definición de la función
def saludar():
    print("Saludo desde la funcion") # el cuerpo de la función está indentado 

saludar() # Llamada de la función

#.................................................

# Ejercicio resuelto N112
# Problema: .
print()
print("-"*40)
print("Programa N112: crear una función que muestre la suma de 2 + 3")
print("-"*40)

def sumar():
    print(2+3)

sumar()
#.................................................

# Ejercicio resuelto N113
# Problema: .
print()
print("-"*40)
print("Programa N113: crear una función que sume dos numeros")
print("-"*40)

def sumar_dosnumeros():
    n1 = int(input('Introduzca el primer número: '))
    n2 = int(input('Introduzca el segundo número '))
    print("La Suma es: ")
    print(n1+n2)
    # Podemos colocar mas de una instrucción dentro de la función

sumar_dosnumeros()

#.................................................

# Ejercicio resuelto N114
# Problema: .
print()
print("-"*40)
print("Programa N114: Llamar a las funciones de los ejercicios 111, 112, 113")
print("-"*40)
print()
print("Ejercicio Llamada de varias funciones")

print("Función del ejercicio 111")
saludar()

print("Función del ejercicio 112")
sumar()

print("Función del ejercicio 113")
sumar_dosnumeros()

#..............................................
# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / noviembre - 2020 / pythoncumanes
