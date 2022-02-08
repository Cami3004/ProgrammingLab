class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
       righe=[] #inizializzo una lista vuota
       for line in my_file:
           righe.append(line)
       return righe
       my_file.close()

my_file=open('sales.txt', 'r')
csv_file=CSVFile('sales.txt') #csv_file è un'istanza
print('Nome del file: {}'. format(csv_file.name))
print('Dati contenuti nel file: {}'.format(csv_file.get_data()))