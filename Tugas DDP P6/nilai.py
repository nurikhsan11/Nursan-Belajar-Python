#program untuk menghitung nilai

#input
nama = input("masukkan nama anda ? ")
kelas = input("massukkan kelas anda ? ") 
nilai = int(input("massukkan nilai anda ? "))

# proses keterangan
if nilai > 89 and nilai < 101:
    ket="nilai anda istimewa"
elif nilai > 59 and nilai < 70:
    ket="nilai anda cukup"
elif nilai > 69 and nilai < 90:
    ket="nilai anda sangat bagus"
else :
    ket="anda gagal"

#output
print("nama saya adalah " ,nama)
print("kelas saya adalah" ,kelas)
print("nilai saya adalah" ,nilai)
print("dinyatakan" ,ket)

    