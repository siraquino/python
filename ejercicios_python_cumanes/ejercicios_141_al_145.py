# Ejercicios resueltos del 141 al 145
# Ejercicios de FOR (para)/ Contadores

#.................................................
# Ejercicio resuelto N141
print()
print("-"*44)
print("Programa N141: Generar: 1 2 3 4 5 6 7 8 9 10")
print("-"*44)

n = 0
for i in range(1,11):
    n = n + 1
    print(n, end = " ")
print()

#.................................................
# Ejercicio resuelto N142
print()
print("-"*44)
print("Programa N142: Generar: 10 9 8 7 6 5 4 3 2 1")
print("-"*44)

n = 11
for i in range(1,11):
    n = n - 1
    print(n, end = " ")
print()
#.................................................
# Ejercicio resuelto N143
print()
print("-"*44)
print("Programa N143: Generar: 1 4 2 3 3 2 4 1")
print("-"*44)

asc = 0
des = 5
for i in range(1,5):
    asc = asc + 1
    des = des -1
    print(asc,des,"",end = "")
print()
print("Segunda forma")
des = 5
for i in range(1,5):
    des = des -1
    print(i,des,"",end = "")
print()    
print("Tercera forma")
print()
asc = 0
for i in range(4,0,-1):
    asc = asc + 1
    print(asc,i,"",end = "")
#.................................................
# Ejercicio resuelto N144
print()
print("-"*44)
print("Programa N144: Generar: 1 2 3 x 5 6 7")
print("y contar los numeros colocados y cuantas letras")
print("-"*44)
contarLetras = 0
contarnNumeros = 0
x = ' '
for i in range(1,8):
    if i == 4:
        print('x',end = " ")
        contarLetras = contarLetras + 1
    else:
        print(i,'',end = "")
        contarnNumeros = contarnNumeros + 1
print()
print("Se colocaron: ", contarnNumeros, "Numeros")
print("Se coloco: ", contarLetras, "Letra")
print()
#.................................................
# Ejercicio Resuelto N145 de Pythoncumanes
# Tema: Contadores
print()
print("-"*44)
print("Programa N145: Generar: 1 2 3 4 5 4 3 2 1 ")
print("-"*44)
yo_cambio = 0
for i in range(1,10):
    if i <= 5:
        yo_cambio = yo_cambio + 1
        print(yo_cambio,'',end = "")
    else:
        yo_cambio = yo_cambio - 1
        print(yo_cambio,'',end = "")
#OBSERVACION
# Estos Ejercicios no me los sé de memoria, no hace falta (Sirven para desarrollar la lógica)
# Los realicé analizando cado uno, disfruté haciendo el 144 y el 145
# Es recomendable el uso del lápiz y papel para hacer las series y ver el comportamiento
# Ejercicio resuelto N145
print()
print("-"*44)
print("BONUS: Generar: 5 4 3 2 1 2 3 4 5 ")
print("-"*44)
yocambio = 6
for i in range(1,10):
    if i <= 5:
        yocambio = yocambio - 1
        print(yocambio,'',end = "")
    else:
        yocambio = yocambio + 1
        print(yocambio,'',end = "")
    
#########################
# Puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / febrero - 2021 / pythoncumanes