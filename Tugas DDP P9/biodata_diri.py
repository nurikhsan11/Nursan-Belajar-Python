# Biodata Diri dengan metode Fungsi menggunakan python

def biodata(nama,alamat,tanggal_lahir,umur,Tinggi_Badan):
    bb_ideal = str((int(Tinggi_Badan) - 100)-((int(Tinggi_Badan)- 100) * 0.10))
    print("nama  : "+nama)
    print("alamat  : "+alamat)
    print("tanggal lahir : "+tanggal_lahir)
    print("umur : "+umur)
    print("tinggi badan : "+Tinggi_Badan)
    print('berat badan ideal: '+ bb_ideal)
    
biodata("ikhsan","Depok","12 juni 2006","16","169")