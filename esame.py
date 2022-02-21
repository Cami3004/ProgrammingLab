class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        #controllo che il tipo di name sia una stringa
        if not isinstance(name,str):
            raise ExamException('Errore, name non è una stringa')
        self.name=name

    def get_data(self):
        #provo ad aprire il file e controllo che il file esista
        try:
            my_file=open(self.name, 'r')
            my_file.readline()
        except:
            raise ExamException('Errore, file non apribile')
            return None
        
        #controllo che il file non sia vuoto ???? NON STAMPA NIENTE
        if not my_file:
            raise ExamException('Errore, il file inserito è vuoto')

        #inizializzo una lista vuota per salvare tutti i dati
        time_series=[]
        #leggo il file linea per linea, faccio lo split di ogni riga sulla virgola in modo da separare la data dal numero dei passeggeri
        for line in my_file:
            elementi=line.split(',')
            #Pulisco il carattere di newline dall'ultimo elemento con la funzione strip(), che in realtà toglie anche gli spazi bianchi all'inizio e alla fine di una stringa
            elementi[-1]=elementi[-1].strip()
            #se non sto processando l'intestazione...
            if elementi[0]!='date':
                #controllo che ci siano almeno due elementi, ovvero la data e il numero di passeggeri, cioè controllo che la linea sia completa
                if(len(elementi)>=2):
                    data=elementi[0]
                    passeggeri=elementi[1]
                #controllo che la data abbia sia un anno che un mese
                    data=data.split('-')
                    if(len(data)>=2):
                        anno=data[0]
                        mese=data[1]
                    #dato che ha sia un anno che un mese controllo se il loro tipo è valido con isnumeric che restituisce True se tutti i caratteri in una stringa sono numeri
                    #controllo anche che il mese sia compreso tra 1 e 12 e che l'anno sia positivo
                        if (anno.isnumeric()==True and mese.isnumeric()==True):
                            if(int(anno)>0 and int(mese)>=1 and int(mese)<=12):
                                    anno=int(anno)
                                    mese=int(mese) #perchè dovrei convertirli ad intero???
                            else: 
                                print('Errore riscontrato nella seguente data: {}-{}'.format(anno, mese))
                                continue
                        else: 
                            print('Errore riscontrato nella seguente data: {}-{}'.format(anno, mese))
                            continue #con l'istruzione continue termino l'iterazione e continuo con il prossimo ciclo ignorando questa riga come da consegna
                        
                        #controllo, come da consegna, che il numero di passeggeri sia intero positivo
                        if (passeggeri.isnumeric()==True and int(passeggeri)>0):
                            passeggeri=int(passeggeri)
                        else:
                            print('Errore, questo valore dei passeggeri non è intero positivo: {}'.format(passeggeri))
                            continue

            time_series.append([f"{anno}-{mese}",passeggeri]) #in questo modo inserisco la data sotto forma di stringa mentre il numero dei passeggeri come numero
            #spiegare o sostituire zfill, ma effettivamente serve?????
           
        my_file.close()
        #ora ho tutti i dati "puliti", cioè ho tutti i dati che cercato (data,passeggeri)
        #creo una lista per salvere solo le date e non i numeri di passeggeri e controllo se ci sono duplicati con la funzione count()
        #(FORSE POCO EFFICIENTE)
        lista_date=[]
        for item in time_series:
            lista_date.append(item[0])
         
        for item in lista_date:
            if(lista_date.count(item)>1):
                raise ExamException('Errore, la seguente data è ripetuta: {}'.format(item))
        #ora controllo se è ordinata
        #anno e mese in questo mese sono stringhe sono int ed esistono????
        return time_series

def detect_similar_monthly_variations(time_series, years):
    #controllo la validità della lista years:
    #controllo che years sia una lista
    if not isinstance(years, list):
            raise ExamException('Errore, i valori non sono inseriti in una lista, ma si tratta di: {}'.format(type(years)))
    #controllo che la lista abbia precisamente due valori
    if (len(years)!=2):
        raise ExamException('Errore, la lista inserita non può essere considerata perchè non ha due due valori ma ne ha: {}'.format(len(years)))
    #controllo che i due valori siano degli interi
    if (isinstance(years[0], int)==False or isinstance(years[1], int)==False):
        raise ExamException('Errore, gli elementi della lista devono essere due numeri interi')

    if (years[0]<1949 or years[1]>1960):
        raise ExamException("Errore, l'intervallo non è valido, perchè si stanno considerando degli anni non appartenenti al file")
    if(years[0]>=years[1]):
        raise ExamException('Errore, range di anni non valido')
    if(years[1]-years[0]!=1):
        raise ExamException('Errore, range di anni non valido perchè i due anni inseriti devono essere consecutivi')

#se sono arrivata qui significa che il range di anni inseriti è valido
#ora creo una lista di liste di tre elementi con anno,mese,passeggeri, partendo da time_series
    lista_dati=[]
    for item in time_series:
        riga_dati=[]
        for i,element in enumerate(item):
            if i==0:
                anno_mese=element.split('-')
                riga_dati.append(int(anno_mese[0]))
                riga_dati.append(int(anno_mese[1]))
            else:
                riga_dati.append(element)
                continue
    
            lista_dati.append(riga_dati)

    #utilizzo list comprehension per creare due liste con il mese e il numero dei passeggeri per quel mese considerando solo i due anni years[0] e years[1] inseriti in input
    passeggeri_anno_0=[[item[1],item[2]] for item in lista_dati if item[0]==years[0]]
    passeggeri_anno_1=[[item[1], item[2]] for item in lista_dati if item[0]==years[1]]

    #creo due liste di 12 elementi in cui ogni elemento sarà la stringa 'nullo'
    anno0_passeggeri=[]
    anno1_passeggeri=[]
    for v in range(12):
        anno0_passeggeri.append('nullo')
    for v in range(12):
        anno1_passeggeri.append('nullo')

    #ora sostituisco il valore 'nullo' con il numero dei passeggeri di quel mese (mese 1=gennaio, posizione 0) e nel caso in cui manca un valore rimane la stringa 'nullo'
    #faccio due volte la stessa cose perchè ho due liste, una per years[0] e una per years[1]
    for item in passeggeri_anno_0:
        mese=int(item[0])
        anno0_passeggeri[mese-1]=item[1]

    for item in passeggeri_anno_1:
        mese=item[0]
        anno1_passeggeri[mese-1]=item[1]

    differenza_anno0=[]
    for i in range(11):
        if(anno0_passeggeri[i]=='nullo' or anno0_passeggeri[i+1]=='nullo'):
            differenza_anno0.append('nullo')
        else:
            differenza_anno0.append(anno0_passeggeri[i+1]-anno0_passeggeri[i])
    print(differenza_anno0)

    differenza_anno1=[]
    for i in range(11):
        if(anno1_passeggeri[i]=='nullo' or anno1_passeggeri[i+1]=='nullo'):
            differenza_anno1.append('nullo')
        else:
            differenza_anno1.append(anno1_passeggeri[i+1]-anno1_passeggeri[i])
    print(differenza_anno1)

    risultato=[]
    for i in range (11):
        if(differenza_anno0[i]=='nullo' or differenza_anno1[i]=='nullo'):
            risultato.append(False)
        elif(differenza_anno0[i]-differenza_anno1[i] in range(-2,3)): #metto range(-2,3) perchè l'estremo superiore non è compreso
            risultato.append(True)
        else:
            risultato.append(False)
    print(risultato)


csv_file=CSVTimeSeriesFile('data.csv') 
time_series=csv_file.get_data()
lista=[1950,1951]
result=detect_similar_monthly_variations(time_series,lista)