from w3_1 import Mobil
from w3_3 import Kucing
    
class mahasiswa:
    def __init__(self, nim, nama, prodi, alamat):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.alamat = alamat
        # self.mobil = mobil
        # self.kucing = kucing

    def perkenalan(self):
        print("=" * 30)
        print("Nama Saya     : {}".format(self.nama))
        print("NPM           : {}".format(self.nim))
        print("Prodi         : {}".format(self.prodi))
        print("alamat        : {}".format(self.alamat))
        print("=" * 30)



