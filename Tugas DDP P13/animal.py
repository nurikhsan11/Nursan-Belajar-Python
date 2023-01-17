class Animal:
    name = ""
    makanan = ""
    hidup = ""
    berkembang_biak = ""
    
    def __init__ (self,name,makanan,hidup,berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def cetak (self):
        print("Nama = ",self.name)
        print("makanan = ",self.makanan)
        print("habitat hewan ini di = ",self.hidup)
        print("hewan ini berkembang biak dengan cara = ",self.berkembang_biak)
        
