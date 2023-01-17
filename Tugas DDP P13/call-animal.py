from animal import *
from badak import *
from ikan import *
from ular import *

b1 = badak("badak bercula satu","tunas","darat","beranak","Dataran rendah","hewan yang dilindungi")
b1.cetak()
b1.bernafas()
b1.karakteristik()
b1.jenis()

print(f"="*50)

i1 = ikan("ikan","jentik nyamuk","air","bertelur","Sungai danau,telaga dan laut","hewan yang dilindungi")
i1.cetak()
i1.bernafas()
i1.berenang()

print(f"="*50)

u1 = ular("ular","daging rumput dan lain lain","darat dan air","bertelur","Hutan sawah dan perairan","hewan yang dilindungi")
u1.cetak()
u1.bernafas()
u1.karakteristik()
u1.jenis()