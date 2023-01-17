#program kalkulator 

a=int(input("masukkan angka 1    =  "))
b=int(input("masukkan angka 2   =  "))
c=int(input("pilih opsi operator 1/2/3/4/5 = "))

#Rumus
if c==1 :
    d= a + b
    print("hasil operator penjumlahan   =  ",d)
elif c==2 :
    e= a - b
    print("hasil operator pengurangan   =  ",e)
elif c==3 :
    f= a / b
    print("hasil operator pembagian   =  ",f)
elif c==4 :
    g = a * b
    print("hasil operator perkalian   =  ",g)
elif c==5 :
    h= a ** b
    print("hasil operator pangkat   =  ",h)
