class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio=1):
        #controllo che l'argomento opzionale ratio sia un numero
        if not (isinstance(ratio,int) or isinstance(ratio,float)):
            raise ExamException('errore, il valore inserito per la variabile ratio "{}" non è valido perchè non è nè del tipo int e nemmeno float'.format(ratio))
        #controllo che il ratio inserito sia un numero maggiore di zero
        if ratio<1:
            raise ExamException('il ratio inserito "{}" non è un numero maggiore di zero, quindi verrà fissato uguale a 1 di default'.format(ratio))
            ratio=1
        self.ratio=ratio

    def compute(self, lista):
        #controllo che la lista non sia vuota
        if not lista:
            raise ExamException('Errore, la lista inserita è vuota')
        #controllo che la lista sia del tipo lista, ovvero che i valori siano inseriti in una lista
        if not isinstance(lista, list):
            raise ExamException('Errore, i valori non sono inseriti in una lista, ma si tratta di: {}'.format(type(lista)))
        #controllo che la lista non contenga un solo numero
        if (len(lista)==1):
            raise ExamException('Errore, la lista contiene un solo elemento e quindi è impossibile calcolare diff')
        #controllo che la lista contenga solo numeri interi o floating point
        for item in lista:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise ExamException("errore, l'elemento della lista {} non è un numero".format(item))
        
        risultato=[]
        for i in range(len(lista)-1):
            risultato.append((lista[i+1]-lista[i])/self.ratio)
        #ritorno la lista con i risultati
        return risultato

lista=[2,4,8,16]
diff=Diff(2)
risultato=diff.compute(lista)
print(risultato)