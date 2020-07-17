# Ejercicios resueltos del 028 al 030

# Los ejercicios del 028 al 030
#......................................................
# Ejercicio resuelto N028
# Problema: Si sumamos 1234 y 243 y le restamos 67.¿Cúal será   
# el resultado?
print("Programa N028: Sumar 1234 + 243 y restarle 67")
n1 = 1234
n2 = 243
n3 = 67
operacion =(n1+n2)-n3 
print("El resultado es: ",operacion)
print()
# Intenta hacerlo de otra manera, puede ser usando
# suma = n1+n2 y luego operacion = suma - n3 
#...................................................

# Ejercicio resuelto N029
# Problema: Rodrigo compró a crédito unos zapatos por Bs. 10.000.000.
# Si hasta hora ha pagado 3.700.000. ¿Cúanto dinero debe a la zapatería?
print("Programa N029: Compra a crédito")
valor = 10000000 #No se coloca puntos!
abono = 3700000
debe = valor - abono 
print("Debe a la zapatería: ",debe,"Bolívares" )
print()
#...................................................

# Ejercicio resuelto  N030
# Problema: Ismael compró una camisa por Bs. 500.000,40 y una franela 
# por 400.000,10. Si pagó con un cheque y en su cuenta tiene 1.000.000,70.
#¿Cúanto dinero le queda en la cuenta? 
print("Programa N030: Cuenta Corriente")
tiene = 1000000.70 #los decimales se colocan con punto
camisa = 500000.40
franela = 400000.10
queda = tiene-(camisa + franela) 
print("El Saldo en la cuenta Corriente es: ",queda,"Bolívares" )
print()
#...................................................

#
# Primero cópialos como están escritos, luego intenta modificar sus valores para practicar
#Rafael Aquino / mayo-2020 / pythoncumanes