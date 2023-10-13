class kucing:
    def __init__(self, usia, warna ):
        self.usia = usia
        self.warna = warna
# method
    def mengeong(self):
        print("Kucing {} dengan usia {} bulan".format(self.warna, self.usia ))

kucing1 = kucing(8, "coklat")
kucing2 = kucing(5, "putih")
kucing3 = kucing(10, "oren")
kucing1.mengeong()
kucing2.mengeong()
kucing3.mengeong()
