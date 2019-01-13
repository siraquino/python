print("Triangulo de Floyd")
x=0
y=1
for i in range(1,16):
    print()
    for j in range(1,x):
        if y<10:
            print(y,end="  ")
        else:
            print(y,end=" ")
        y=y+1
    x=x+1
print()
print("@siraquino")
print ("Fin d el programa")