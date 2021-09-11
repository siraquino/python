# Ejercicios resueltos del 146 al 150
# Ejercicios de While (mientras)/ 

#.................................................
# Ejercicio resuelto N146
print()
print("-"*44)
print("Programa N146: Generar: 1 2 3 4 5 6 7 8 9 10")
print("-"*44)
print("Primera forma")
i = 1
while i <= 10:
    print(i, end = " ")
    i = i + 1
print()

print("Segunda forma")
i = 0
while i < 10:
    i = i + 1
    print(i, end = " ")
print()

print("Tercera forma")
flag = True
i = 1
while flag == True:
    if i <=10:
        print(i, end = " ")
        i = i + 1
    else:
        flag = False    
print()

print("Tercera forma 2")
flag = True
i = 1
while flag:
    if i <=10:
        print(i, end = " ")
        i = i + 1
    else:
        flag = False    
print()
#.................................................
# Ejercicio resuelto N147
# Pythoncumanes
print()
print("-"*44)
print("Programa N147: Generar: 0 1 0 1 0 1 0 1 0 1")
print("-"*44)
n = 10
bandera = True
while n > 0:
    if bandera:
        print(0, end = " ")
        bandera = False
    else:
        print(1, end = " ")
        bandera = True
    n = n - 1
#.................................................
# Ejercicio resuelto N148
# Pythoncumanes
print()
print("-"*44)
print("Programa N148: Generar: 2 4 6 8 10 12 14 16 18 20")
print("-"*44)
print("Primera Forma") 
n = 1
while n <=10:
    print(n*2, end = " ")
    n = n + 1
print()    
print("Segunda Forma") 
n = 1
while n <=20:
    if n % 2 == 0: 
        print(n, end = " ")
    n = n + 1    
#.................................................
# Ejercicio resuelto N149
# Pythoncumanes
print()
print("-"*44)
print("Programa N149: Generar: 3 6 9 12 15 18 21")
print("-"*44)
print("Primera Forma") 
n = 1
while n < 8:
    print(n*3, end = " ")
    n = n + 1
print()    
print("Segunda Forma") 
n = 1
while n <=21:
    if n % 3== 0: 
        print(n, end = " ")
    n = n + 1    
# Ejercicio resuelto N150
# Pythoncumanes
print()
print("-"*44)
print("Programa N150: Generar: -5  5  -4  4  -3  3  -2  2  -1  1")
print("-"*44)
n = -5
while n < 0:
    print(n, end = "  ")
    print(abs(n), end = "  ")
    n = n + 1    

# Recuerda Mucha Creatividad, Mucha Creatividad!

#########################
# Puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / marzo - 2021 / pythoncumanes