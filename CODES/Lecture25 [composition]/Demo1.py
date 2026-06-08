# class 1
class Mobil:
    # parameter constructor
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
        self.pemilik = None

    def display(self):
        print("Mobil:", self.merk, "Tahun:", self.tahun)
        if self.pemilik:
            self.pemilik.display()

# class 2
class Pemilik:
    # parameter constructor
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    def display(self):
        print("Pemilik:", self.nama, "Alamat:", self.alamat)

# Membuat objek Pemilik
pemilik1 = Pemilik("Semmy Taju", "Jl. yordan No. 123")

# Membuat objek Mobil
mobil1 = Mobil("Toyota Avanza", 2023)

# Menghubungkan objek Mobil dengan objek Pemilik
mobil1.pemilik = pemilik1

# Menampilkan informasi mobil beserta pemiliknya
mobil1.display()

