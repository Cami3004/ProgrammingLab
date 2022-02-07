def somma_valori(self):
    #inizializzo una lista vuota per salvare i valori
    values=[]

    #agisco linea per linea
    for line in my_file:
        #faccio lo split di ogni riga sulla virgola
        elements=line.split(',')
        #se NON sto processando l'intestazione (che sono delle parole e non ci servono)
        if elements[0]!='Date':
            value=elements[1]
            #aggiungo alla lista dei valori che era vuota questo valore
            values.append(float(value)) #con float sto trasformando le stringhe in numeri in modo da poter fare la somma
    my_file.close()
    somma=0
    for item in values:
        somma=somma+item
    return (somma)

#apro e leggo il file
my_file = open('sales.txt', 'r')
print(somma_valori(my_file))