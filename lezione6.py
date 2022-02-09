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
        
    def get_data(self, start=5, end=7):
        #se nell'init ho settato can_read a False vuol dire che il file non poteva essere aperto, quindi lo comunico ed esco dalla funzione tornando 'niente'
        if self.can_read==False:
            print('Errore, file non apribile o illeggibile')
            return None
        
        else: #altrimenti inizializzo una lista vuota per salvare tutti i dati
            my_file = open(self.name, 'r')
            dati=[]
            #leggo il file linea per linea, faccio lo split di ogni riga sulla virgola
            for line in my_file:
                elements=line.split(',')
                #se non sto processando l'intestazione aggiungo alla lista gli elementi di questa linea
                if elements[0]!='Date':
                    dati.append(elements)
            for i in range(5,7,1):
                print(dati[i])
                #in questo modo il numero finale non viene considerato, mentre se voglio considerarlo devo scrivere: i=start while i<=end: print(dati[i]) i=i+1
        #devo controllare che start sia minore di end, che siano entrambi due numeri maggiori di zero (al massimo start uguale a zero), che siano due numeri interi, o stringhe convertibili a interi, se sono float li arrotondo avvisando, che, se start è minore di end, allora verifico che end sia minore uguale alla lunghezza totale della lista
        my_file.close()

    
csv_file=CSVFile('sales.txt') #csv_file istanza
print('Nome del file: {}'.format(csv_file.name))
print('Contenuto del file: "{}"'. format(csv_file.get_data()))