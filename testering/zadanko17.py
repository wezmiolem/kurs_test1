class Pipeline:
    def __init__(self, values: list):
        self.values = values
    def FiltrowanieDodatnich(self):
        self.values = [x for x in self.values if x>0]
    def zaokraglacz(self):
        self.values = [round(x) for x in self.values]
    def skalowanie(self,factor=2):
        self.values = [x*factor for x in self.values]
    def sumowanie(self):
        return sum(self.values)
    
rurociag = Pipeline([1.7, -3.2, 5.8, -1.1, 8.3, 2.4])
print(rurociag.values)
rurociag.FiltrowanieDodatnich()
print(rurociag.values)
rurociag.zaokraglacz()
print(rurociag.values)
rurociag.skalowanie(3)
print(rurociag.values)
suma = rurociag.sumowanie()
print(suma)
