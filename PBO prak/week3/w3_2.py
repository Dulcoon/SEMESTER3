from w3_1 import Mobil
from w3_3 import Kucing
    
class mahasiswa:
    def __init__(self, nim, nama, prodi, alamat, mobil, kucing):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.alamat = alamat
        self.mobil = mobil
        self.kucing = kucing

    def perkenalan(self):
        print("=" * 30)
        print("Nama Saya     : {}".format(self.nama))
        print("NPM           : {}".format(self.nim))
        print("Prodi         : {}".format(self.prodi))
        print("alamat        : {}".format(self.alamat))
        print("merk mobil    : ",self.mobil.merk)
        print("warna mobil   : ",self.mobil.warna)
        print("tahun mobil   : ",self.mobil.tahun)
        print("Saya punya kucing bernama", self.kucing.nama, "Berjenis", self.kucing.jenis)
        print("=" * 30)


a = input("NIM ")
b = input("Nama ")
c = input("Prodi ")
d = input("alamat ")
a1 = input("Merk Mobil ")
b1 = input("warna ")
c1 = input("Tahun ")
d = input("Nama Kucing ")
e = input("Jenis Kucing ")

mhs1 = mahasiswa(a,b,c,d, 
                 Mobil(a1, b1, c1),
                 Kucing(d,e)
                 )
mhs1.perkenalan()

