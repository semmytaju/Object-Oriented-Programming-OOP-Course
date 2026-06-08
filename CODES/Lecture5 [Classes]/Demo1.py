# create a clss
class Produk():
    # variable
    jumlah_produk = 0
    
    # method constructor (default method)
    def __init__(self, nama, harga):
        self.nama = nama;
        self.harga = harga;
                
    # method #1
    def view_jum_produk(self, jumlah):
        Produk.jumlah_produk = jumlah;
        print('Total Produk: ', Produk.jumlah_produk);
    
    # method #2
    def detail_produk(self):
        print("Nama : ", self.nama);
        print("Harga: ", self.harga);
        
        
# membuat objek pertama (Object instantiation)
produk1 = Produk('Kerupuk', 5000)

# membuat objek kedua (Object instantiation)
produk2 = Produk('Taro', 3000)        
        
# membuat objek ketiga (Object instantiation)
produk3 = Produk('Astor', 4000)        

# mengakses attribut objek (Accessing class attributes) 
produk1.detail_produk()
produk1.view_jum_produk(5)
print("Jumlah produk adalah {}".format(produk1.__class__.jumlah_produk));
print("Nama produk adalah {}".format(produk1.nama))
print()

produk2.detail_produk()
produk2.view_jum_produk(10)
print("Jumlah produk adalah {}".format(produk2.__class__.jumlah_produk));
print("Nama produk adalah {}".format(produk2.nama))
print()

produk3.detail_produk()
produk3.view_jum_produk(15)
print("Jumlah produk adalah {}".format(produk3.__class__.jumlah_produk));
print("Nama produk adalah {}".format(produk3.nama))


