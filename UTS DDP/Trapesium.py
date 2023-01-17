#Program menghitung luas dan keliling Trapesium 

a= int(input("masukkan alas dari trapesium     =   "))
c= int(input("masukkan sisi yang sejajar dengan alas    =   "))
t= int(input("masukkan tinggi dari trapesium    =  "))
aa=int(input("masukkan sisi 1  =  "))
ab= int(input("masukkan sisi 2  =  "))
ac=int(input("masukkan sisi 3  =  "))
ad=int(input("masukkan sisi 4  =  "))

#Rumus 
luas= 1/2 * (a+c) * t
keliling= aa + ab + ac + ad

print("luas trapesium adalah     =    ",luas)
print("keliling trapesium adalah     =    ",keliling)

