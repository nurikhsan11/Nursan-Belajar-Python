#Program untuk pemesanan di restoran

#input
Namapembeli= input("massukkan nama anda = ")
Nohppembeli= input("massukan no hp anda = ")
tanyamenu= input("Pesan menu apa? ")
#proses pesan menu apa 
if tanyamenu == "makanan" :
    print("Nasi Goreng = RP. 15.000")
    print("Mie Goreng = RP. 12.000")
    print("Ayam Geprek = RP. 18.000")
elif tanyamenu == "minuman" :
    print("Aneka jus = RP. 15.000")
    print("softdrink = RP. 10.000")
    print("sweet ice tea = RP. 5.000")
pesan = input("massukkan pesanan anda = ")
jumlahpesanan= int(input("massukkan jumlah pesanan anda = ")) 
#proses
#_____________makanan____________
if pesan == "Nasi Goreng" :
    harga= 15000 * jumlahpesanan
elif pesan == "Mie Goreng" :
    harga = 12000 * jumlahpesanan
elif pesan == "Ayam Geprek" :
    harga = 18000 * jumlahpesanan
#____________minuman____________
if pesan == "Aneka jus" :
    harga = 15000 * jumlahpesanan
elif pesan == "softdrink" :
    harga = 10000 * jumlahpesanan
elif pesan == "sweet ice tea" :
    harga = 5000 * jumlahpesanan
#output
print("Nama pemesan = " ,Namapembeli)
print("No hp pemesan = " ,Nohppembeli)
print("menu yang anda pesan = " ,pesan)
print("Total pesanan = " ,jumlahpesanan)
print("anda harus membayar seharga =  ",harga)


