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

            time_series.append([f"{anno}-{str(mese).zfill(2)}",passeggeri]) #in questo modo inserisco la data sotto forma di stringa mentre il numero dei passeggeri come numero
            #spiegare o sostituire zfill
           
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
    
        return time_series

def detect_similar_monthly_variations(time_series, years):
    #oppure posso mettere fist_year=years[0] e last_years=years[1]
    #controllo la validità della lista years:
    #controllo che years sia una lista
    if not isinstance(years, list):
            raise ExamException('Errore, i valori non sono inseriti in una lista, ma si tratta di: {}'.format(type(years)))
    #controllo che la lista abbia precisamente due valori
    if (len(years)!=2):
        raise ExamException('Errore, la lista inserita non può essere considerata perchè non ha due due valori ma ne ha: {}'.format(len(years)))
    else: #ha senso mettere if dentro else o no??
        #controllo che i due valori siano degli interi
        if not (isinstance(years[0], int) or isinstance(years[1], int)):
            raise ExamException('Errore, gli elementi della lista devono essere due numeri interi')

        if (years[0]<1949 or years[1]>1960):
            raise ExamException("Errore, l'intervallo non è valido, perchè si stanno considerando degli anni non appartenenti al file")
        elif(years[0]>=years[1]):
            raise ExamException('Errore, range di anni non valido')

        
#my_file=open('data.csv', 'r')
csv_file=CSVTimeSeriesFile('data.csv') 
print('Dati contenuti nel file: {}'.format(csv_file.get_data()))