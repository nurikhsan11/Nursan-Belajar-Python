class kantin:
    def __init__(self):
        self.menu_makanan = {
            "oreo" : 8000,
            "sari gandum" : 6000,
            "bakso" : 12000,
            "nasi goreng" : 15000,
            "mie ayam" : 12000
        }
        self.menu_minuman = {
            "es teh" : 5000,
            "es jeruk" : 7000,
            "jus alpukat" : 12000,
            "es kukubima" : 5000,
            "es cappucino" : 15000
        }
        
    def cetak_struk (self, nama, uang, pesanan):
        total_harga = 0
        for a in pesanan:
            total_harga += a["harga"]
        print(f"nama = {nama}")
        print("pesanan:")
        for a in pesanan:
            print(f'{a["nama"]} {a["jumlah"]} x {a["harga"]} = {a["jumlah"]} * {a["harga"]}')
        print(f'total harga = {total_harga}')
        print(f'uang yang dibawa = {uang}')
        print(f'kembalian: {uang - total_harga}')
    
class konsumen:
    def __init__(self, nama, uang):
        self.nama = nama
        self.uang = uang
        
    def pesan(self, kantin, pesanan):
        items = []
        for a in pesanan:
            item = {
                "nama" : a,
                "jumlah" : pesanan[a],
                "harga" : kantin.menu_makanan[a] if a in kantin.menu_makanan else kantin.menu_minuman[a]
            }
            items.append(item)
            
        total_harga = 0
        for item in items:
            total_harga += item['jumlah'] * item['harga']
            
        if total_harga > self.uang:
            print('maaf, uang anda tidak cukup.')
        else:
            kantin.cetak_struk(self.nama, self.uang, items)
        