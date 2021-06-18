frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)

for i in (range(0,len(frutas))):
    print(next(iterador,len(frutas)))

