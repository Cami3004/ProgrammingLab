class CSVFile():
    def __init__(self, name):
        self.name=name
        #provo ad aprirlo e a leggere una riga
        self.can_read=True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
            if type(my_file.name)!=str:
                raise Exception ('Il nome del file non è una stringa e invece è: "{}"'.format(type(my_file.name)))
        except Exception as e:
            self.can_read=False
            print('Errore in apertura del file: {}'.format(e))
        
    def get_data(self):
        #se nell'init ho settato can_read a False vuol dire che il file non poteva essere aperto, quindi lo comunico ed esco dalla funzione tornando 'niente'
        if self.can_read==False:
            print('Errore, file non apribile o illeggibile')
            return None
        
        else: #altrimenti inizializzo una lista vuota per salvare tutti i dati
            my_file = open(self.name, 'r')
            dati=[]
            #leggo il file linea per linea, faccio lo split di ogni riga sulla virgola
            s=0 #in s memorizzo il numero di linee del file
            for line in my_file:
                s=s+1
                elements=line.split(',')
                #se non sto processando l'intestazione aggiungo alla lista gli elementi di questa linea
                if elements[0]!='Date':
                    try:
                        dati.append(elements)
                    except:
                        raise Exception ('Non è stato possibile convertire il valore "{}" in un elemento della lista'.format(elements))
                        break
            try:
                start=int(input("Inserisci l'inizio dell'intervallo: "))
            except Exception as e:
                print('"{}"" non è convertibile in intero'.format(start))
                print('Ho trovato questo errore: {}'.format(e))
            if not isinstance(start, int) or (start<0):
                raise Exception('{} non è un numero intero positivo'.format(start))
            if (start>s):
                raise Exception('{} è più grande del numero di linee del file che sono: {}'.format(start,s))
            try:
                end=int(input("Inserisci la fine dell'intervallo: "))
            except Exception as e:
                print('"{}" non è convertibile in intero'.format(end))
                print('Ho trovato questo errore: {}'.format(e))
            if not isinstance(end, int) or (end<0):
                raise Exception('"{}" non è un numero intero positivo'.format(end))
            if(end>s):
                raise Exception ('{} è più grande del numero di linee del file che sono: {}'.format(end, s))
            if(start>end):
                raise Exception ("La fine dell'intervallo {} è minore del suo inizio {}".format(end, start))
            return dati[start:end]
        #devo controllare che start sia minore di end, che siano entrambi due numeri maggiori di zero (al massimo start uguale a zero), che siano due numeri interi, o stringhe convertibili a interi, se sono float li arrotondo avvisando, che, se start è minore di end, allora verifico che end sia minore uguale alla lunghezza totale della lista
        my_file.close()

    
csv_file=CSVFile('sales.txt') #csv_file istanza
print('Nome del file: {}'.format(csv_file.name))
print('Contenuto del file: "{}"'. format(csv_file.get_data()))