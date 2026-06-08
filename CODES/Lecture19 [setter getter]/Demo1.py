# create class
class Perpustakaan:
    def __init__(self):
        self.__nama = "";
        self.__jumlah_buku = 0;

    def set_nama(self, nama):
        if nama == "Unklab":    
            self.__nama = "Juan Mambu";
        elif nama == "Klabat":    
            self.__nama = "Semmy Taju";
        else:    
            self.__nama = nama;


    def get_nama(self):
        if self.__nama == "Semmy Taju":
            return "He is a lecturer.";
        else:
            return "He/she is a student.";

    def set_jumlah_buku(self, jumlah_buku):
        self.__jumlah_buku = jumlah_buku;

    def get_jumlah_buku(self):
        return self.__jumlah_buku;
    
# Membuat objek perpus1 dari class Perpustakaan
perpus1 = Perpustakaan()

# Mengatur nilai atribut menggunakan setter
perpus1.set_nama("Klabat")
perpus1.set_jumlah_buku(10000)

# Mengakses nilai atribut menggunakan getter
nama_perpus = perpus1.get_nama()
jumlah_buku = perpus1.get_jumlah_buku()
print("Nama perpustakaan:", nama_perpus)
print("Jumlah buku di perpustakaan:", jumlah_buku)

# Mengubah nilai atribut menggunakan setter
perpus1.set_jumlah_buku(15000)

# Mengakses nilai atribut setelah diubah menggunakan getter
jumlah_buku = perpus1.get_jumlah_buku()
print("Jumlah buku di perpustakaan setelah diubah:", jumlah_buku)


