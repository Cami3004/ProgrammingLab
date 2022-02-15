class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, lunghezza): 
        #controllo che la lunghezza inserita sia un intero
        if not isinstance(lunghezza, int): #oppure potevo scrivere if (isinstance(lunghezza,int)==False)
            raise ExamException ("L'unico tipo accettato per la variabile lunghezza è int, mentre '{}' è del tipo {}".format(lunghezza, type(lunghezza)))
        #controllo che la lunghezza inserita sia un numero maggiore di zero
        if (lunghezza<1): #che è come scrivere lunghezza<=0
            raise ExamException ('errore, è stato inserito un numero minore o uguale a zero. Il valore "{}" non è valido'.format(lunghezza))

        self.lunghezza=lunghezza

    def compute(self,lista):
        #controllo che la lista non sia vuota
        if not lista: #oppure controllavo che la sua lunghezza non fosse zero
            raise ExamException('Errore, la lista inserita è vuota')
        #controllo che i valori siano in una lista
        if not isinstance(lista, list):
            raise ExamException('I valori non sono inseriti in una lista, ma si tratta di: {}'.format(type(lista)))
        #controllo che la lista sia più lunga della finestra
        if(self.lunghezza>len(lista)):
            raise ExamException('errore, la lista è più corta della finestra')
        #controllo che i valori inseriti nella lista siano di tipo float o int
        for item in lista:
            if not(isinstance(item,float) or isinstance(item,int)):
                raise ExamException("L'elemento {} non è nè di tipo intero e nemmeno di tipo floating point".format(item))
        
        risultato=[] #lista vuota
        #calcolo la media mobile ciclando su tutti gli elementi della lista
        for i in range(len(lista)+1):
            #se non ho abbastanza valori su cui applicarla continuo andando al prossimo giro (cioè fino a quando non ottengo la lunghezza della finestra)
            if i<self.lunghezza:
                continue
            else:
                media=0
                #osservazione: l'elstremo superiore i non è compreso
                media=sum(lista[i-self.lunghezza:i])/self.lunghezza
                risultato.append(media)
        
        return risultato
    
media_mobile=MovingAverage(2)
lista=[2,4,8,16]
risultato=media_mobile.compute(lista)
print(risultato) 