# Ejercicios resueltos del 123 al 125
# Trabajaremos con Condicionales
#.................................................
# Ejercicio resuelto N123

print()
print("-"*40)
print("Programa N123: Determinar si una persona es menor o mayor de edad")
print("-"*40)

edad = int(input("Introduzca su edad: "))

if edad >= 18:
    print("Es Mayor de edad")
else:
    print("Es Menor de edad")
print("Se usó el condicional edad >= 18") 
#.................................................

# Ejercicio resuelto N124
# Igual al ejercicio anterior, modificando la condición
print()
print("-"*40)
print("Programa N124: Determinar si una persona es menor o mayor de edad - Otra forma")
print("-"*40)

edad = int(input("Introduzca su edad: "))

if edad < 18: # aquí preguntamos primero si es menor
    print("Si es Menor de edad")
else:
    print("Si es Mayor de edad")

print("Se usó el condicional edad < 18") 

#.................................................

# Ejercicio resuelto N125
# 
print()
print("-"*40)
print("Programa N125: Sumar dos números si son iguales")
print("-"*40)

numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))

if numero1 == numero2: 
    print("Como son iguales se suman")
    print("La suma es: ", numero1 + numero2)
else:
    print("No son igual por tal motivo no se sumaron")

#..............................................
##### PRACTIQUEMOS CON FUNCIONES
##### EJERCICIO 125 SEGUNDA FORMA - CON FUNCIONES 
print("EJERCICIO 125 CON FUNCIONES - CONDICIONALES")
print("Sumar dos números si son iguales")

def leer():
    """Para leer número"""
    n = int(input("Introduzca un número: "))
    return n


def suma(x,y):
    """Suma dos números"""
    return x + y


numero1 = leer() 
numero2 = leer()

if numero1 == numero2:
    print(suma(numero1,numero2))
    print("Como son iguales se sumaron")
else:
    print("No son igual, por tal motivo, no se sumaron")


# Puedes intentar tu forma de hacerlo con funciones
# Este lo modifiqué varias veces.
# A veces la primera vez no corre (cualquier programa)
# pero viendo los errores e intentándolo varias veces se aprende.
# A partir de ahora (con el uso de los condicionales)
#   nuestra lógica empieza a mejorar.  



# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / enero - 2021 / pythoncumanes
