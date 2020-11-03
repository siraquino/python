# Ejercicios resueltos del 101 al 105

#.................................................
# Ejercicio resuelto N101
# Problema: Calcular el Valor absoluto de un número
print()
print("-"*40)
print("Programa N101: Calcular el Valor absoluto de un número")
print("-"*40)

n = int(input('Introduzca el número: '))

print('El Valor absoluto del número', n, 'es',abs(n))

#.................................................
# Ejercicio resuelto N102
# Problema: Determinar si el número 10 es un entero
print()
print("-"*40)
print("Programa N102: Determinar si el número 10 es un entero")
print("-"*40)

es = isinstance(10, int) 
print(es)
#..............................................
# Ejercicio resuelto N103
# Problema: Determinar si el número '10' es un entero
print()
print("-"*40)
print("Programa N103: Determinar si '10' es un string")
print("-"*40)

es = isinstance('10', str) 
print(es)
#..............................................
# Ejercicio resuelto N104
# Problema: Calcular el Valor absoluto de un número
print()
print("-"*40)
print("Programa N104: Redondear un número")
print("-"*40)

r = float(input('Introduzca número decimal: '))

print('El Valor redondeado de', r, 'es',round(r))
#..............................................
# Ejercicio resuelto N105
# Ayuda de python

#Entra en la ayuda
#help()
 
"""
Ejemplo: Estando dentro de la ayuda 
help> print
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

help>
"""
#Para salir quit ó Ctl + C
#.................

#información de print() directamente y no se queda en la ayuda
help(print)
#puedes praticar este comando en la consola de python

#..............................................
# A partir de ahora puedes practicar en la web https://repl.it/ (debes
# registrarte) allí podras guardar todos tus ejercicios. Tanto los del curso
# como los que tu inventes!.  
# Si tienes alguna duda, contáctame
# Rafael Aquino / octubre - 2020 / pythoncumanes
