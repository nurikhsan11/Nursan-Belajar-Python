from animal import *
class ikan(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,status):
        super().__init__(name,makanan,hidup,berkembang_biak)
        self.habitat = habitat
        self.status = status
        
    def bernafas(self):
        print(f"{self.name} bernafas dengan = insang")
        
    def berenang(self):
        print(f"{self.name} hewan ini berenang dengan = sirip")
        
    def cetak (self):
        super().cetak()
        print(f"Habitatnya di {self.habitat}")
        print(f"status hewan ini adalah {self.status}")