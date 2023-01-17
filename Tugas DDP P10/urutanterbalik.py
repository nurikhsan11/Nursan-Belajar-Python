# mengurutkan urutan terbalik (dari belakang)

list_buah_urut = (['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
list_buah_terbalik = []

def reversed(list_buah_urut,list_buah_terbalik):
    for i in range(len(list_buah_urut)):
      dibalik = len(list_buah_urut) -1-i
      list_buah_terbalik.append(list_buah_urut[dibalik])
    
reversed(list_buah_urut, list_buah_terbalik)   
print("list buah awal yaitu =   ",list_buah_urut)
print("list buah akhir yaitu =  ",list_buah_terbalik)