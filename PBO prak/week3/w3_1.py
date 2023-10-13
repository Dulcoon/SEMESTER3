class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
    def kelilingKota(self):
        print("Mobil dengan merk {} berwarna {} tahun {}, terpantau sedang berkelling kota".format(self.merk, self.warna, self.tahun))

