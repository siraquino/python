# Ejercicios resueltos del 060 al 064

# Ejercicios del 060 al 064: String
#......................................................

# Ejercicio resuelto N060
# Problema: Dada una tarjeta que contiene cuatro grupos de digitos 
# se desea crear una varible para cada subgrupo de cuatro dígitos    
print()
print("Programa N060: Dividir variable en subgrupos ")
tarjeta = '1234 2341 3412 4123' 
variable1 = tarjeta[0:4]
variable2 = tarjeta[5:9]
variable3 = tarjeta[10:14]
variable4 = tarjeta[15:19]
print("Variable original: " + tarjeta)
print()
print("Variable1: " + variable1)
print("Variable1: " + variable2)
print("Variable1: " + variable3)
print("Variable1: " + variable4)
print()
#..................................................
# Ejercicio resuelto N061
# Problema: Determinar el número de caracteres de una palabra
print()
print("Programa N061:Determinar el número de caracteres de una palabra ")
palabra = 'Electroencefalografista'
numero_de_caracteres = len(palabra)
print("La palabra " + palabra + " " + "Tiene ", numero_de_caracteres, "caracteres")
print()
#...................................................
# Ejercicio resuelto N062
# Problema: Dado una clave de tres caracteres, invertir la clave   
print()
print("Programa N062: Invertir clave")
clave = '1b9'
clave_invertida = clave[-1] + clave[-2] + clave[-3] 
print("La clave es: " + clave)
print("La clave invertida es: " + clave_invertida)
print()
#...................................................

# Ejercicio resuelto N063
# Problema: Determinar el número de caracteres de una frase
print ()
print("Programa N063: Determinar el número de caracteres de una frase")
frase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
n_de_caracteres = len(frase)
print("La Frase " + frase + " " + "Tiene: ", n_de_caracteres, "caracteres")
#...................................................
print ()
# Ejercicio resuelto N064
# Problema: Dada Dada una frase aplicar 2 funciones internas 
# para el tratamiento de cadenas de caracteres 
print("Programa N064: Dos funciones para string")
print ()
frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print('*'*71)
print("Frase Original: " + frase)
print('*'*71)
print ()
print("Aplicando frase.title()")
print(frase.title())
print ()
print("Aplicando frase.upper()")
print(frase.upper())
print ()
print ()
#...................................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar
#Rafael Aquino / junio-2020 / pythoncumanes