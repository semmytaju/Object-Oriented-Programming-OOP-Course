# create class #1
class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = [] # empty array
    
    def tulis_buku(self, judul):
        buku = Buku(judul, self.nama) # create object buku
        self.daftar_buku.append(buku)
  
# create class #2
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

# object dari class Penulis
penulis1 = Penulis("Semmy Taju")

# daftar buku-buku
penulis1.tulis_buku("Java Programming")
penulis1.tulis_buku("Data Structures in Python")
penulis1.tulis_buku("Machine Learning Algoritms")

# Mengakses daftar buku dan informasi penulis
for buku in penulis1.daftar_buku:
    print("Judul Buku:", buku.judul)
    print("Penulis Buku:", buku.penulis)
    print()



