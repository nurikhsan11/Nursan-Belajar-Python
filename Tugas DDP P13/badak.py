from animal import *
class badak(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,status):
        super().__init__(name,makanan,hidup,berkembang_biak)
        self.habitat = habitat
        self.status = status
        
    def bernafas(self):
        print(f"{self.name} bernafas dengan = paru-paru ")
        
    def karakteristik(self):
        print(f"{self.name} karakter hewan ini adalah = herbivora ")
        
    def jenis(self):
        print(f"{self.name} jenis hewan ini adalah = mamalia ")
        
    def cetak (self):
        super().cetak()
        print(f"Habitatnya di =  {self.habitat}")
        print(f"status hewan ini adalah =  {self.status}")