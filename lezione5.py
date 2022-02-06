class CSVFile():
    def __init__(self, name):
        self.name=name
        try:
            my_file = open(self.name, 'r')
        except FileNotFoundError:
            print('Non posso aprire il file perchè il file non esiste')
    def get_data(self):
       my_file = open(self.name, 'r')
       righe=[] #lista vuota
       for line in my_file:
           righe.append(line)
       return righe 
    
csv_file=CSVFile('sales.txt') #csv_file istanza
print('Contenuto del file: "{}"'. format(csv_file.get_data()))

