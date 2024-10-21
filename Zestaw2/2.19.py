def fill_to_three(lista):
    line = ""
    for i in range (0,len(lista)):
        if(len(str(lista[i])) < 3):
            line = line + str(lista[i]).zfill(3) + " "
        else:
            line = line + str(lista[i]) + " "
    lista1 = line.split()
    return lista1


lista = [ 5, 35, 568, 54, 321, 3 , 8 ]
print(fill_to_three(lista))
