def al_reves(b):
	c=[]
	for y in range(len(b)):
		c.append(b[(len(b)-y)-1])
	
	print("Nueva lista invertida")
	print(c)
		

a = [10,20,30,40,50,60,70]

print("Lista Original")
print(a)
al_reves(a)

#Rafael_Aquino