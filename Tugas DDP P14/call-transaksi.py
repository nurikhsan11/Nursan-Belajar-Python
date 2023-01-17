from transaksi import *

kantin = kantin()

konsumen1 = konsumen("srikumala",50000)
konsumen1.pesan(kantin, {"nasi goreng" : 2, "es jeruk" : 1})

konsumen2 = konsumen("nursan",30000)
konsumen2.pesan(kantin, {"nasi goreng" : 1, "es teh": 2, "oreo" : 1})