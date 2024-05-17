class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        self.kuliah = []
        
    def tambah_mata_kuliah(self, mata_kuliah):
        if mata_kuliah.kuota > 0:
            self.kuliah.append(mata_kuliah)
            mata_kuliah.kurangi_kuota()
            print(f"Mahasiswa {self.nama} berhasil menambah Mata Kuliah {mata_kuliah.nama}. \nKode MK: {mata_kuliah.kode} \nJumlah SKS: {mata_kuliah.jmlSks} SKS")
            print(f"Sisa kuota mata kuliah {mata_kuliah.nama}: {mata_kuliah.kuota}\n")
        else:
            print(f"Maaf, kuota mata kuliah {mata_kuliah.nama} telah penuh.\n")
    
    def hapus_mata_kuliah(self, mata_kuliah):
        if mata_kuliah in self.kuliah:
            self.kuliah.remove(mata_kuliah)
            mata_kuliah.tambah_kuota()
            print(f"Mahasiswa {self.nama} berhasil menghapus Mata Kuliah {mata_kuliah.nama}.")
            print(f"Sisa kuota mata kuliah {mata_kuliah.nama}: {mata_kuliah.kuota}\n")
    
    def list_mata_kuliah(self):
        print(f"List mata kuliah {self.nama}:")
        for mk in self.kuliah:
            print(f"- {mk.nama} ({mk.kode})")

class MataKuliah:
    def __init__(self, nama, kode, jmlSks, kuota):
        self.nama = nama
        self.kode = kode
        self.jmlSks = jmlSks
        self.kuota = kuota

    def kurangi_kuota(self):
        if self.kuota > 0:
            self.kuota -= 1
    
    def tambah_kuota(self):
        self.kuota += 1

m1 = Mahasiswa("Divany Pangestika", "2215061036", "Teknik Informatika")
m2 = Mahasiswa("Amelia Putri", "2215061088", "Teknik Informatika")

mk1 = MataKuliah("Pemrograman Berorientasi Objek", "INF620213", 4, 2)
mk2 = MataKuliah("Kecerdasan Buatan", "INF620215", 3, 1)

m1.tambah_mata_kuliah(mk1)
m1.tambah_mata_kuliah(mk2)
print("\n")

m2.tambah_mata_kuliah(mk1)
print("\n")

print("Sebelum penghapusan:")
m1.list_mata_kuliah()
m2.list_mata_kuliah()
print("\n")

#Menghapus mata kuliah pada mahasiswa 1
m1.hapus_mata_kuliah(mk1)

print("\nSetelah penghapusan:")
m1.list_mata_kuliah()
    