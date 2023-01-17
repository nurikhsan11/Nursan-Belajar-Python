# Loop For and Range belajar

baris = int(input('Jumlah baris yang ingin diulang: '))
for i in range (baris) :
    for j in range (i+1) :
        print ('*', end='')
    print ('')