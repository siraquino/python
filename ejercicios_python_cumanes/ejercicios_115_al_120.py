# Ejercicios resueltos del 115 al 120
# Trabajaremos con Funciones creadas por nosotros
# Parámetros - Argumentos 
#.................................................
# Ejercicio resuelto N115
# Problema: crear una función que muestre un saludo personalizado
print()
print("-"*40)
print("Programa N115: crear una función que muestre un saludo personalizado")
print("-"*40)
#definición de la función
def mensaje(nombre): #nombre es el Parámetro
    print("Hola " + nombre)  


mensaje("Rafael") # Llamada de la función con Argumento
#Como ejercicio lee el nombre de la persona desde el teclado
# y realiza el llamado de la función
#.................................................

# Ejercicio resuelto N116
# Problema: crear una función que sume: a) 23 + 2; b) 45 + 34 y c) 24 + 56
print()
print("-"*40)
print("Programa N116: crear una función que sume: a) 23 + 2; b) 45 + 34 y c) 24 + 56")
print("-"*40)

def sumar(a,b): 
    print('La Suma de ', a , ' + ', b, 'es ', a + b)  


sumar(23,2) 
sumar(45,34)
sumar(24,56)
# Revisa el ejercicio 112. A medida que avanzamos vamos 
# optimizando y mejorando nuestros ejercicios.
# Tenemos más herramientas para hacer nuestros programas
#.................................................

# Ejercicio resuelto N117
# Problema: Leer el nombre y la edad de dos personas y mostrarlos
print()
print("-"*40)
print("Programa N117: Leer el nombre y la edad de dos personas y mostrarlos")
print("-"*40)

def mostrar(n,e): 
    print('El nombre es', n)  
    print('La edad es', e)  


def leer():
    nombre = input("Teclee su nombre ")
    edad = int(input('Teclee su edad '))
    mostrar(nombre,edad) 

leer()
leer()
#.................................................

# Ejercicio resuelto N118
# Problema: Leer dos números y determinar quien es el mayor y el menor
print()
print("-"*40)
print("Programa N118: Leer dos números y determinar quien es el mayor y el menor")
print("-"*40)

def mayor_menor(n1,n2): 
    print('El Mayor es', max(n1,n2))  
    print('El Menor es', min(n1,n2))
    #max() y min() son funciones predefinidas de python  
    

def leer_numeros():
    numero1 = int(input("Primer Número "))
    numero2 = int(input("Segundo Número "))
    mayor_menor(numero1,numero2) 

leer_numeros()
#.................................................

# Ejercicio resuelto N119
# Problema: Leer tres números y ordenarlos de menor a mayor
print()
print("-"*40)
print("Programa N119: Leer tres números y ordenarlos de menor a mayor")
print("-"*40)

def ordenar(n1,n2,n3): 
    mayor = max(n1,n2,n3)
    menor = min(n1,n2,n3)
    #...
    suma = n1 + n2 + n3 
    centro = suma - mayor - menor
    #... Artificio para conseguir el del centro       
    print("Números Ordenados de menor a mayor") 
    print(menor, centro, mayor) 
    

def leer_numeros():
    numero1 = int(input("Primer Número "))
    numero2 = int(input("Segundo Número "))
    numero3 = int(input("Segundo Número "))
    ordenar(numero1,numero2,numero3) 

leer_numeros()
#.................................................

# Ejercicio resuelto N120
# Problema: Leer tres números y ordenarlos de mayor a menor
print()
print("-"*40)
print("Programa N120: Leer tres números y ordenarlos de mayor a menor")
print("-"*40)

def ordenar(n1,n2,n3): 
    mayor = max(n1,n2,n3)
    menor = min(n1,n2,n3)
    #...
    suma = n1 + n2 + n3 
    centro = suma - mayor - menor
    #... Artificio para conseguir el del centro       
    print("Números Ordenados") 
    print(mayor, centro, menor) 
    

def leer_numeros():
    numero1 = int(input("Primer Número "))
    numero2 = int(input("Segundo Número "))
    numero3 = int(input("Segundo Número "))
    ordenar(numero1,numero2,numero3) 

leer_numeros()

# Intenta hacen un solo ejercicio que una el 119 y 120.

#..............................................
# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / noviembre - 2020 / pythoncumanes
