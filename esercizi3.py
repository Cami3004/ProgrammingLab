class Automobile():
    def __init__ (self, casa_automo, modello, numero_posti, targa):
        self.casa_automo=casa_automo
        self.modello= modello
        self.numero_posti= numero_posti
        self.targa=targa

    def __str__(self):
        return 'Casa auto: {}\nModello: {}\nNumero posti: {}\nTarga:{}'.format(self.casa_automo, self.modello, self.numero_posti, self.targa)
        
    def parla(self):
        print('Broom Broom')

    def confronta(self):
        if auto_1.casa_automo==auto_2.casa_automo:
            print('le due auto sono della stessa casa automobilistica')
        if auto_1.modello == auto_2.modello:
            print('le due auto sono dello stesso modello')
        if auto_1.numero_posti==auto_2.numero_posti:
            print('le due auto hanno lo stesso numero di posti')

class Transformer(Automobile):
    def __init__ (self, nome, generazione, grado, reparto):
        self.nome=nome
        self.generazione=generazione
        self.grado=grado
        self.reparto=reparto

    def scheda_militare(self):
        print('Nome: {}\nGenerazione: {}\nGrado: {}\nReparto: {}'.format(self.nome, self.generazione, self.grado, self.reparto))

    
auto_1 = Automobile('fiat', '500', '5', 'AY567V')
auto_2 = Automobile('fiat', '500', '4', 'CD673X')
print(auto_1)
print(auto_2)
auto_1.parla()
auto_1.confronta()
trans = Transformer('transformer_1', '2', 'sergente', 'spionaggio')
#print(trans)
trans.scheda_militare()
