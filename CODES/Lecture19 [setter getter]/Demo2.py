# create class #1
class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def tulis_buku(self, judul):
        print(f"{self.nama} menulis buku dengan judul {judul}")

# creae class #2
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def cetak_info(self):
        print(f"Buku '{self.judul}' ditulis oleh {self.penulis.nama} dari {self.penulis.alamat}")


# create objects dari class Penulis dan class Buku
penulis1 = Penulis("Semmy Wellem Taju", "Manado")
buku1 = Buku("Java Programming", penulis1)

# info buku
buku1.cetak_info() 

# info penulis
penulis1.tulis_buku("Java Programming") 


