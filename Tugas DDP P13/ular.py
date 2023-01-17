from animal import *
class ular(Animal):
    def __init__(self,name,makanan,hidup,berkembang_biak,habitat,status):
        super().__init__(name,makanan,hidup,berkembang_biak)
        self.habitat = habitat
        self.status = status
        
    def bernafas(self):
        print(f"{self.name} bernafas dengan = paru-paru ")
        
    def karakteristik(self):
        print(f"{self.name} karakter hewan ini adalah = omnivora ")
        
    def jenis(self):
        print(f"{self.name} jenis hewan ini adalah = Reptil ")
        
    def cetak (self):
        super().cetak()
        print(f"Habitatnya di {self.habitat}")
        print(f"status hewan ini adalah {self.status}")