class CSVFile():
    def __init__(self, name):
        self.name=name
    def get_data(self):
       my_file = open(self.name, 'r')
       righe=[] #lista vuota
       for line in my_file:
           righe.append(line)
       return righe 
    
csv_file=CSVFile('sales.txt') #csv_file istanza
print(csv_file.get_data())

