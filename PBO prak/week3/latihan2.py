class matkul:
    def __init__(self, data_matkul):
        self.data_matkul = data_matkul

    def tampilkan_matkul(self):
        for matkul in self.data_matkul:
            print(matkul)


class kucing:
    def __init__(self, warna, usia) :
        self.warna = warna
        self.usia = usia
    
class mahasiswa:
    def __init__(self, nama, jurusan, kucingMhs, dataMatkul):
        self.nama = nama
        self.jurusan = jurusan
        self.kucingMhs = kucingMhs
        self.dataMatkul = matkul(dataMatkul)

    def perkenalan(self):
        print("Hallo, perkenalkan nama saya {}, saya mhs jurusan {}".format(self.nama, self.jurusan))
        print("Saya memiliki kucing berwarna {}, dengan usia {} bulan".format(self.kucingMhs.warna, self.kucingMhs.usia ))
        print("Nilai saya antara lain : ")
        self.dataMatkul.tampilkan_matkul()


data = ["PBO", "Pemrograman WEB", "Sistem Digital", "Basis data"]

mhs1 = mahasiswa(
    "valen",
    "informatika",
    kucing(warna="putih",
           usia="8"
           ),
    data
)

mhs1.perkenalan()