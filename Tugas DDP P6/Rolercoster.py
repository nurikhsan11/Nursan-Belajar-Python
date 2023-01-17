#program menggunakan logika if untuk permainan roler coster

#input
nama = input("masukkan nama anda=  ")
umur = input("masukkan umur anda=  ")
tinggi =int(input("masukkan tinggi anda= "))

#logika
if (tinggi>90):
    ket="boleh bermain roler coster"
else:
    ket=" tidak boleh bermain roler coster"
#output
print("nama saya = " ,nama)
print("umur saya = " ,umur)
print("tinggi saya = " ,tinggi)
print("diperbolehkan bermain roler coster/tidak?" ,ket)

