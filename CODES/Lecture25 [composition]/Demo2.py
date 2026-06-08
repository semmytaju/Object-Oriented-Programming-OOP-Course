# class 1
class Mobil:
    # parameter constructor
    def __init__(self, jenis, warna):
        self.jenis = jenis
        self.warna = warna

# class 2
class Pemilik:
    # parameter constructor
    def __init__(self, nama, mobil):
        self.nama = nama
        self.mobil = mobil

    # method 1
    def tampilkan_data(self):
        print("Nama Pemilik:", self.nama)
        print("Jenis Mobil:", self.mobil.jenis)
        print("Warna Mobil:", self.mobil.warna)

# Membuat objek Mobil
mobil1 = Mobil("Toyota Avanza", "Merah")

# Membuat objek Pemilik
pemilik1 = Pemilik("Semmy Taju", mobil1)

# Menampilkan informasi mobil beserta pemiliknya
pemilik1.tampilkan_data()

