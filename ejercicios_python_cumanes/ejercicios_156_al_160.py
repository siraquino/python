# Ejercicios resueltos del 156 al 160
# Ejercicios Diccionarios

#.................................................
# Ejercicio resuelto N156

print()
print("-"*44)
print("Programa N156: Generar el dicionario = {1:'10',2:'20',3:'30',4:'40'}")
print("-"*44)

diccionario = {1:"10",2:"20",3:"30",4:"40"}
print(diccionario)

#.................................................
# Ejercicio resuelto N157

print()
print("-"*44)
print("Programa N157: Generar un diccionario con nombre jugador")
print("donde las claves son nombre, edad, sexo")
print("y los valores son Rafael, 50, M ")
print("-"*44)

jugador = {"nombre":"Rafael","edad":50,"sexo":"M"}
print(jugador)
  
#.................................................
# Ejercicio resuelto N158

print()
print("-"*44)
print("Programa N158: Generar un diccionario con nombre jugador")
print("donde las claves son nombre, edad, sexo")
print("y los valores son Rafael, 50, M ")
print("Luego cambiar los valores por Sofía, 22, F ")
print("-"*44)

jugador = {"nombre":"Rafael","edad":50,"sexo":"M"}
print("Jugador Inicial")
print(jugador)
jugador["nombre"] = "Sofía"
jugador["edad"] = "22"
jugador["sexo"] = "F"
print("Jugador final")
print(jugador)


#.................................................
# Ejercicio resuelto N159

print()
print("-"*44)
print("Programa N158: Generar un diccionario donde los valores sean diccionarios")
print("Usted decide el modelo")
print("-"*44)

alumnos = {"alumno":{1:"Rafael",2:"sofía"},"notas":{1:16,2:17}}
print(alumnos)

#.................................................
# Ejercicio resuelto N160

print()
print("-"*44)
print("Programa N158: Generar un diccionario donde los valores sean listas")
print("Usted decide el modelo")
print("-"*44)

numeros = {"positivos":[1,56,9,3],"negativos":[-2,-4,-76]}
print(numeros)

  
# Recuerda Mucha Creatividad, Mucha Creatividad!

#########################
# Puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / marzo - 2021 / pythoncumanes