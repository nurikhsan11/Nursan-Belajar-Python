#Buat program jenis bensin harga bensin ke kota tujuan

PLite=10000
PMax=14000
PTurbo=17000
JtempuhPLite=12
JtempuhPMax=13
JtempuhPTurbo=13.5
Jakarta=20
Bekasi=35.7
Depok=5
Tangerang=99
Bogor=120.6
Hasilpakai=0
Totalharga=0

#input 
Namaken=input("Nama kendaraan yang digunakan ")
J_Bensin=input("jenis bensin yang digunakan ")
Kotatuju=input("Kota yang dituju ")

#proses
if {J_Bensin== "pertalite"} :
    Hasilpakai = eval(Kotatuju) / JtempuhPLite
    Totalharga = Hasilpakai * PLite
elif {J_Bensin== "pertamax"}:
    Hasilpakai = eval(Kotatuju) / JtempuhPMax
    Totalharga = Hasilpakai * PMax
elif {J_Bensin == "pertamax turbo"}:
    Hasilpakai = eval(Kotatuju) / JtempuhPTurbo
    Totalharga = Hasilpakai * PTurbo
else :
    print={"ERROR"}

#ROUNDING NUMBER
Hasilpakai = round(Hasilpakai ,2)
Totalharga = round(Totalharga)

#output
print("Nama kendaraan yang digunakan" ,Namaken)
print("Jenis bensin yang digunakan" ,J_Bensin)
print("Kota yang dituju" ,Kotatuju)
print("Hasil pemakaian" ,Hasilpakai)
print("Total harga dari bensin" ,Totalharga)