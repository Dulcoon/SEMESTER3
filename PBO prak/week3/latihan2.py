class matkul:
    def __init__(self, matkul):
        self.matkul = matkul

class kucing:
    def __init__(self, warna, usia) :
        self.warna = warna
        self.usia = usia
    
class mahasiswa:
    def __init__(self, nama, jurusan, kucingMhs, dataMatkul):
        self.nama = nama
        self.jurusan = jurusan
        self.kucingMhs = kucingMhs
        self.dataMatkul = dataMatkul

    def perkenalan(self):
        print("Hallo, perkenalkan nama saya {}, saya mhs jurusan {}".format(self.nama, self.jurusan))
        print("Saya memiliki kucing berwarna {}, dengan usia {} bulan".format(self.kucingMhs.warna, self.kucingMhs.usia ))
        print("Saya mengambil beberapa mata kuliah, diantara nya : {}".format(self.dataMatkul))


data = 
for i in data:
    print(i)

mhs1 = mahasiswa(
    "valen",
    "informatika",
    kucing(warna="putih",
           usia="8"
           ),
    matkul()
)

mhs1.perkenalan()