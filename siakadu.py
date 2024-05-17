class Mahasiswa:
    def __init__(self, nama, npm, prodi):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        self.kuliah = []
        
    def tambah_mata_kuliah(self, mata_kuliah):
        self.kuliah.append(mata_kuliah)
        self.mata_kuliah = mata_kuliah
        mata_kuliah.tambah_mahasiswa(self)
    
    def hapus_mata_kuliah(self, mata_kuliah):
        if mata_kuliah in self.kuliah:
            self.kuliah.remove(mata_kuliah)
            mata_kuliah.hapus_mahasiswa(self)
    
    def list_mata_kuliah(self):
        print(f"List mata kuliah {self.nama}:")
        for mk in self.kuliah:
            print(f"- {mk.nama} ({mk.kode})")

class MataKuliah:
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode
        self.mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        if mahasiswa not in self.mahasiswa:
            self.mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, mahasiswa):
        if mahasiswa in self.mahasiswa:
            self.mahasiswa.remove(mahasiswa)

    def list_mahasiswa(self):
        print(f"List mahasiswa di mata kuliah {self.nama}:")
        for mhs in self.mahasiswa:
            print(f"- {mhs.nama} ({mhs.npm})")

m1 = Mahasiswa("Divany Pangestika", "2215061036", "Teknik Informatika")
m2 = Mahasiswa("Amelia Putri", "2215061088", "Teknik Informatika")

mk1 = MataKuliah("Pemrograman Berorientasi Objek", "INF620213")
mk2 = MataKuliah("Kecerdasan Buatan", "INF620215")

m1.tambah_mata_kuliah(mk1)
m1.tambah_mata_kuliah(mk2)
print("\n")

m2.tambah_mata_kuliah(mk1)
print("\n")

m1.list_mata_kuliah()
print("\n")

m2.list_mata_kuliah()
print("\n")

mk1.list_mahasiswa()
print("\n")

mk2.list_mahasiswa()  
    