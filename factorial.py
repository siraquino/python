#Factorial de los 10 primeros numeros naturales
f=0
fact=1
c=0
while f < 11:
    f=f+1
    print("El factorial de: ", c, "= ", fact)
    c=c+1
    x=f
    fact=1
    while x >=1:
        fact=fact*x
        x=x-1
print("@siraquino")
print("Fin del Programa")