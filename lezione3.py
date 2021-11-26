def somma_valori(array_values):
    array_values=[]

    for line in my_file:
        elements=line.split(',')
        if elements[0]!='Date':
            value=elements[1]
            array_values.append(float(value))
    my_file.close()
    somma=0
    for prezzo in array_values:
        somma+=prezzo
    return (somma)

my_file = open('sales.txt', 'r')
print(somma_valori(my_file))  