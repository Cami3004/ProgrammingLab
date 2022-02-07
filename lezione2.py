lista_numeri=[4,5,6,7,9]

def sum_lista(lista_numeri):
    somma=0
    for item in lista_numeri:
        somma=somma+item
    return somma

print ('La somma degli elementi della lista è: {}'.format(sum_lista(lista_numeri)))