from Gempa import *
# Object
gempa1 = data_Gempa("Banten", 1.2)
gempa2 = data_Gempa("Palu", 6.1)
gempa3 = data_Gempa("Cianjur", 5.6)
gempa4 = data_Gempa("Jayapura", 3.3)
gempa5 = data_Gempa("Garut", 4.0)

gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()