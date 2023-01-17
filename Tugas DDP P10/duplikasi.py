# duplikasi list 

nama_buah = (['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) 

def duplicate(nama_buah):
    buah_Duplikat = nama_buah.copy()
    nama_buah[1] = "pepaya"
    nama_buah[2] = "mangga"
    nama_buah[3] = "mangga"
    nama_buah[4] = "pisang"
    
    buah_Duplikat [0] = "pisang"
    buah_Duplikat [1] = "durian"
    buah_Duplikat [2] = "durian"
    buah_Duplikat [3] = "jambu"
    
    hasil_duplikasi = nama_buah + buah_Duplikat
    nama_buah.extend(hasil_duplikasi)
    return hasil_duplikasi

hasil_duplikasi = duplicate(nama_buah)
print("hasil dari buah yang di duplikat adalah =  ",hasil_duplikasi)