def string_of_numbers(lista):
    word = ""
    for i in range(0,len(lista)):
        word += str(lista[i])
    return word

lista = [5, 6 ,5, 4, 3,2, 1, 2,4 ,5]
print(string_of_numbers(lista))
