class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
    def kelilingKota(self):
        print("Merk mobil {}\n warna {}\n tahun {}".format(self.merk, self.warna, self.tahun))

