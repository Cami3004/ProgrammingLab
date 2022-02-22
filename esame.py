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

        #inizializzo una lista vuota per salvare tutti i dati
        time_series=[]
        #leggo il file linea per linea, faccio lo split di ogni riga sulla virgola in modo da separare la data dal numero dei passeggeri
        for line in my_file:
            elementi=line.split(',')
            #Pulisco il carattere di newline dall'ultimo elemento
            elementi[-1]=elementi[-1].strip()
            #se non sto processando l'intestazione...
            if elementi[0]!='date':
                #controllo che ci siano almeno due elementi, ovvero la data e il numero di passeggeri, cioè controllo che la linea sia completa
                if(len(elementi)>=2):
                    data=elementi[0]
                    passeggeri=elementi[1]
                #controllo che la data abbia sia l'anno che il mese
                    data=data.split('-')
                    if(len(data)>=2):
                        anno=data[0]
                        mese=data[1]
                    #controllo che il loro tipo sia valido con isnumeric che restituisce True se tutti i caratteri in una stringa sono numeri
                    #controllo anche che il mese sia compreso tra 1 e 12 e che l'anno sia positivo
                        if (anno.isnumeric()==True and mese.isnumeric()==True):
                            if(int(anno)>0 and int(mese)>=1 and int(mese)<=12):
                                    anno=int(anno)
                                    mese=int(mese)
                            else: 
                                print('Errore riscontrato nella seguente data: {}-{}'.format(anno, mese))
                                continue
                                #con l'istruzione continue termino l'iterazione e continuo con il prossimo ciclo ignorando questa riga come da consegna
                        else: 
                            print('Errore riscontrato nella seguente data: {}-{}'.format(anno, mese))
                            continue
                        
                        #controllo, come da consegna, che il numero di passeggeri sia intero positivo
                        if (passeggeri.isnumeric()==True and int(passeggeri)>0):
                            passeggeri=int(passeggeri)
                        else:
                            print('Errore, questo valore dei passeggeri non è intero positivo: {}'.format(passeggeri))
                            continue

            time_series.append([f"{anno}-{mese}",passeggeri]) #in questo modo inserisco la data sotto forma di stringa mentre il numero dei passeggeri come numero
            
        my_file.close()
        #ora ho tutti i dati "puliti", cioè ho tutti i dati che cercavo (data,passeggeri)
        #creo una lista per salvere le date per intero, una lista per gli anni e un'altra per i mesi
        lista_date=[]
        lista_mesi=[]
        lista_anni=[]
        for item in time_series:
            lista_date.append(item[0])
            anno_mese=item[0].split('-')
            lista_anni.append(int(anno_mese[0]))
            lista_mesi.append(int(anno_mese[1]))

        #controllo che il file non sia vuoto
        if len(lista_date)==0:
            raise ExamException('Errore, il file inserito è vuoto')

        #controllo che non ci siano duplicati con la funzione count() che conta le occorrenze
        for item in lista_date:
            if(lista_date.count(item)>1):
                raise ExamException('Errore, la seguente data è ripetuta: {}'.format(item))

        #controllo che i mesi e gli anni siano in ordine
        #parto da i uguale ad uno saltando il primo elemento perchè non ho nessum dato precedente con cui confrontarlo
        i=1
        while i<(len(lista_date)-1):
            #se le due date hanno lo stesso anno controllo che i mesi siano in ordine crescente
            if(lista_anni[i]==lista_anni[i-1]):
                if lista_mesi[i-1]>lista_mesi[i]:
                    raise ExamException('Errore, la serie temporale non è ordinata')
            #altrimenti se sono passata ad un nuovo anno controllo che esso sia il successivo
            else:
                if lista_anni[i]!=lista_anni[i-1]+1:
                    raise ExamException('Errore, la serie temporale non è ordinata')
            i=i+1

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
#ora creo una lista di liste di tre elementi con anno,mese,passeggeri (tutti di tipo int) partendo da time_series
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
    anno_0=[[item[1],item[2]] for item in lista_dati if item[0]==years[0]]
    anno_1=[[item[1], item[2]] for item in lista_dati if item[0]==years[1]]

    #creo due liste di 12 elementi in cui ogni elemento sarà la stringa 'nullo'
    anno_0_passeggeri=['nullo' for i in range(12)]
    anno_1_passeggeri=['nullo' for i in range(12)]

    #ora sostituisco il valore 'nullo' con il numero dei passeggeri di quel mese (mese 1=gennaio, posizione 0) e nel caso in cui manca un valore rimane la stringa 'nullo'
    #faccio due volte la stessa cose perchè ho due liste, una per years[0] e una per years[1]
    for item in anno_0:
        mese=int(item[0])
        anno_0_passeggeri[mese-1]=item[1]

    for item in anno_1:
        mese=item[0]
        anno_1_passeggeri[mese-1]=item[1]

    #calcolo le differenze come da consegna, considerando che se trovo la stringa 'nullo' c'è un dato mancante e quindi non posso fare la differenza
    diff_anno_0=[]
    #la lista avrà 11 elementi, quindi i andrà da 0 a 10
    for i in range(11):
        if(anno_0_passeggeri[i]=='nullo' or anno_0_passeggeri[i+1]=='nullo'):
            diff_anno_0.append('nullo')
        else:
            diff_anno_0.append(anno_0_passeggeri[i+1]-anno_0_passeggeri[i])
    print(diff_anno_0)

    diff_anno_1=[]
    for i in range(11):
        if(anno_1_passeggeri[i]=='nullo' or anno_1_passeggeri[i+1]=='nullo'):
            diff_anno_1.append('nullo')
        else:
            diff_anno_1.append(anno_1_passeggeri[i+1]-anno_1_passeggeri[i])
    print(diff_anno_1)

    #calcolo la lista finale considerando che se trovo 'nullo' in automatico metto False (come da consegna), altrimenti valuto la variazione
    risultato=[]
    for i in range (11):
        if(diff_anno_0[i]=='nullo' or diff_anno_1[i]=='nullo'):
            risultato.append(False)
        elif(diff_anno_0[i]-diff_anno_1[i] in range(-2,3)):
            risultato.append(True)
        else:
            risultato.append(False)

    return risultato

csv_file=CSVTimeSeriesFile('data.csv') 
time_series=csv_file.get_data()
lista=[1949,1950]
result=detect_similar_monthly_variations(time_series,lista)
print(result)