lista1=[4,5,6,9,7]
lista2=[1,2,3,5,10]

def stampa(lista1):
    print(lista1)

def statistiche(lista1):
    somma=0
    for i in range(len(lista1)):
        type(lista1[i])==int
    somma=sum(lista1)
    minimo=min(lista1)
    massimo=max(lista1)
    print('La somma è: {}, il minimo è: {}, il massimo è: {}'.format(somma, minimo, massimo))

def somma_vettoriale(lista1, lista2):
    my_list=[]
    lunghezza1=len(lista1)
    lunghezza2=len(lista2)
    if lunghezza1==lunghezza2:
        print('Le due liste hanno la stessa lunghezza')
        for i in range(lunghezza1):
            my_list.append(lista1[i] + lista2[i])
        print(my_list)
    else:
        print('Le due liste hanno lunghezze diverse')
        print(my_list)


stampa(lista1)
statistiche(lista1)
somma_vettoriale(lista1, lista2)