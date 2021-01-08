#Para verificar si es par o impar 
def ver_que_es(n):
    if (-1)**n == 1:
        ver_que_es = True # par
    else:
        ver_que_es = False # impar
    
    return ver_que_es


def run():
    cont_par = 0
    cont_impar = 0
    #Cambiar v1 o v2
    for i in (v2):
        print(ver_que_es(i))
        if ver_que_es(i) == True:
            cont_par = cont_par + 1
            atipico_par = i
        else:
            cont_impar = cont_impar + 1
            atipico_impar = i

    if cont_par == 1:
       print(atipico_par)
    else:
       print(atipico_impar)

if __name__ == "__main__":
    v1 = [2, 4, 0, 100, 4, 11, 2602, 36]
    v2 = [160, 3, 1719, 19, 11, 13, -21]
    run()
