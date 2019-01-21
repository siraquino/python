import math 
import os
os.system('cls')
print("5 FORMAS DE MOSTRAR LOS 10 PRIMEROS NUMEROS NATURALES")
print("Primera Forma")
for i in range(1,11):
	print(i, end=" ")
print(); print("Segunda Forma")
j=1
while j <=10:
	print(j, end=" ")
	j=j+1
print(); print("Tercera Forma")	
letras=["A","B","C","D","E","F","G","H","I","J"]
for a in range(10):
	print(ord(letras[a])-64, end= " ")
print(); print("Cuarta Forma")
print(int((4/4)*(4/4)), end= " ")
print(int((4/4)+(4/4)), end= " ")
print(int((4+4+4)/4), end= " ")
print(int((4/4)*((math.sqrt(4))+(math.sqrt(4)))), end= " ")
print(int((4*4+4)/4), end= " ")
print(int(((4+4)/4)+4), end= " ")
print(int((4+4)-4/4), end= " ")
print(int((4/4)*(4+4)), end= " ")
print(int((4/4)+(4+4)), end= " ")
print(int(4+4+4-(math.sqrt(4))), end= " ")
print(); print("Quinta Forma")
x = (1,2,3,4,5,6,7,8,9,10)
z=0; f=True
while f == True:
	print(x[z], end= " ")
	z=z+1
	if z==10:
		f=False	
#@rafa_elaquino