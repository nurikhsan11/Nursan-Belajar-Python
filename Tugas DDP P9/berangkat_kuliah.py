#operator fungsi dengan topik berangkat kuliah dengan python

def berangkat_kuliah():
    kondisi_cuaca = input("jika cuaca hari ini:  ")
    def status():
        if(kondisi_cuaca == "hujan"):
            berangkat = "maka berangkat naik Gocar"
        elif(kondisi_cuaca == "adem"):
            berangkat = "maka berangkat naik motor"
        return berangkat
    print("jika kondisi cuaca: %s" ": %s" %(kondisi_cuaca,status()))
berangkat_kuliah()