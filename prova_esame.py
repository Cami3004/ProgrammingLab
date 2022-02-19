class ExamException(Exception):
    pass

class CSVFile():
     def __init__(self, name):
        self.name=name
        #provo ad aprirlo e a leggere una riga
        self.can_read=True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read=False
            print('Errore in apertura del file: {}'.format(e))

    def get_data(self):
        #se nell'init ho settato can_read a False vuol dire che il file non poteva essere aperto, quindi lo comunico ed esco dalla funzione tornando 'niente'
        if self.can_read==False:
            print('Errore, file non apribile o illeggibile')
            return None
        
        else: #inizializzo una lista vuota per salvare tutti i dati
            my_file = open(self.name, 'r')
            dati=[]
            #leggo il file linea per linea, faccio lo split di ogni riga sulla virgola
            for line in my_file:
                elements=line.split(',')
                elements[-1]=elements[-1].strip() #tolgo gli spazi bianchi all'inizio e alla fine della stringa e tolgo il new line ??????
                #se non sto processando l'intestazione aggiungo alla lista gli elementi di questa linea
                if elements[0]!='date':
                    dati.append(elements)
            return dati
            my_file.close()
    
class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        string_dati=super().get_data() #chiamo la get_data del genitore
        numerical_dati=[] #lista per contenere i dati ma in formato numerico
        #ciclo su tutte le righe del file originale
        for string_row in string_dati:
            #lista di supporto per salvare la riga in formato numerico (tranne il primo elemento)
            numerical_row=[]
            #ciclo su tutti gli elementi della riga con un enumeratore, così ho anche l'indice i della posizione dell'elemento nella riga
            for i, element in enumerate (string_row):
                if i==0:
                    numerical_row.append(element) #il primo elemento della riga lo lascio in formato stringa 
                else: #converto a float tutti gli altri, ma se fallisco stampo l'errore e rompo il ciclo saltando la riga
                    try:
                        numerical_row.append(int(element))
                    except:
                        raise ExamException('Errore, non posso converire il valore "{}" a intero'.format(element))
                        break
            if (len(numerical_row))==len(string_row): #se ho processato tutti gli elementi aggiungo la riga in formato numerico
                numerical_dati.append(numerical_row)
        return numerical_dati

def compute_avg_monthly_difference(time_series, first_year, last_year):
    #controllo che gli anni inseriti sono nel presenti nel file:
    if not first_year in my_file#????
    #controllo che first_year e last_year siano stringhe
    if not (isinstance(first_year,str) or (isinstance(last_year,str))):
        raise ExamException('Errore, una delle due date inserite non è una stringa')
    #provo a convertire ad interi first_year e last_year
    try:
        first_year=int(first_year)
        last_year=int(last_year)
    except:
        raise ExamException('Errore, non è possibile convertire le date ad interi')
    
    if (first_year>last_year):
        raise ExamException("Errore, il primo anno è meggiore dell'ultimo anno")
    

