# Ejercicios resueltos del 126 al 130
# Trabajaremos con Operadores lógicos: not, and, or.
#.................................................
# Ejercicio resuelto N126
print()
print("-"*40)
print("Programa N126: tenemos la variable X = True, invertir su valor ")
print("usando el operador 'not'")
print("-"*40)
print("Primera forma")
X = True
print("El valor Original de X es: ", X)
print("El valor Resultante es: ", not(X))
print()
print()
print("Segunda forma")
X = True
print("El valor Original de X es: ", X)
X = not(X)
print("El valor Resultante es: ", X)
print()
print()
print("Tercera forma")
X = True
print("El valor Original de X es: ", X, " Y su negación es: ", not(X))
# 
#.................................................

# Ejercicio resuelto N127
print()
print("-"*40)
print("Programa N127: Elaborar un programa que determine si una persona")
print("puede tomar un vuelo. La condicion es que tenga boleto y esté vacunado")
print("-"*40)
print("Primera forma")
tieneBoleto = True
tieneVacuna = True
if tieneBoleto == True and tieneVacuna == True:
    print("Puede Tomar el vuelo")
else:
    print("No puede Tomar el vuelo")

print("Segunda forma")
tieneBoleto = True
tieneVacuna = True
if tieneBoleto and tieneVacuna:
    print("Puede Tomar el vuelo, segunda forma")
else:
    print("No puede Tomar el vuelo")
# Intenta hacerlo modificando el valor a tieneBoleto y tieneVacuna
# 
#.................................................

# Ejercicio resuelto N128
print()
print("-"*40)
print("Programa N128: Elaborar un programa que determine si una persona")
print("pagó una mercancia. Puede pagar con tarjeta o efectivo")
print("-"*40)
print("Primera forma")
pagoTarjeta = True
pagoEfectivo = False
if pagoTarjeta == True or pagoEfectivo == True:
    print("Si pagó la mercancia")
else:
    print("No pago la mercancia")
print()
print("Segunda forma")
pagoTarjeta = False
pagoEfectivo = True
if pagoTarjeta == True or pagoEfectivo == True:
    print("Si pagó la mercancia, segunda forma")
else:
    print("No pago la mercancia")
print()
print("Tercera forma")
pagoTarjeta = False
pagoEfectivo = False
if pagoTarjeta == True or pagoEfectivo == True:
    print("Si pagó la mercancia, segunda forma")
else:
    print("No pago la mercancia, tercera forma")
# 
#.................................................

# Ejercicio resuelto N129
print()
print("-"*40)
print("Programa N129: Elaborar un programa que determine si una persona")
print("tiene la edad para poder entrara al ejercito.")
print("Puede si su edad es mayor o igual que 18 y menor o igual a 30")
print("-"*40)
def leer_edad():
    e = int(input("Introduzca tu edad: "))
    return e

edad = leer_edad()
print("La edad es: ", edad)
if edad >= 18 and edad <=30:
    print("Si puede entrar al ejercito")
else:
    print("No puede entrar al ejercito")
# 
#.................................................

# Ejercicio resuelto N130
print()
print("-"*40)
print("Programa N130: Sumar dos números si son pares")
print("-"*40)

numero1 = int(input("Introduzca el primer número: "))
numero2 = int(input("Introduzca el segundo número: "))

if (-1)**numero1 == 1 and (-1)**numero2 == 1: 
    print("Como son Pares se suman")
    print("La suma es: ", numero1 + numero2)
else:
    print("No son pares los dos, por tal motivo no se sumaron")

# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / enero - 2021 / pythoncumanes
