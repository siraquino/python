# Ejercicios resueltos del  055 al 059

# Ejercicios del 055 al 059: String
#......................................................

# Ejercicio resuelto N055
# Problema: Dado tres variables asignadas con tres palabras, concatenarlas en una sola variable   

print()
print("Programa N055: Concatenar palabras")
palabra1 = 'Hola'
print("Palabra1: " + palabra1)
palabra2 = 'cómo'
print("Palabra2: " + palabra2)
palabra3 = 'estás'
print("Palabra3: " + palabra3)
frase = palabra1 + ' ' + palabra2 + ' ' + palabra3
print("La palabra concatenada es: ", frase)
print()
#..................................................
# Ejercicio resuelto N056
# Problema: Visualizar por pantalla
   
print("Programa N056: Visualizar")
print('*')
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)
print('*'*20)
print()
#...................................................
# Ejercicio resuelto N057
# Problema: Determinar la primera letra de una palabra   
print("Programa N057: Determinar la primera letra de una palabra")
palabra = 'Supercalifragilisticoespialidoso'
primera_letra = palabra[0]
print("La Palabra es: " + palabra)
print("La primera letra es: " + primera_letra)
print()
#...................................................
# Ejercicio resuelto N058
# Problema: Determinar la última letra de una palabra
print("Programa N058: Determinar la última letra de una palabra")
p = 'osodilaipseocitsiligarfilacrepus'
print("La palabra es: " + p)
print("La última letra es: " + p[-1])
print ()
#...................................................
# Ejercicio resuelto N059 
# Problema: Dada la palabra Clave $wP12_rTe crear una nueva con los 
# dos primeros caracteres y el último
print("Programa N059: palabra Clave $wP12_rTe")
clave = "$wP12_rTe"
new_clave = clave[0] + clave[1] + clave[-1] 
print("La clave original es: ", clave)
print("La Nueva clave es: ", new_clave)
print ()
#...................................................
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar
#Rafael Aquino / junio-2020 / pythoncumanes