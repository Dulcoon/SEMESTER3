class kucing:
    def __init__(self, usia, warna ):
        self.usia = usia
        self.warna = warna
# method
    def mengeong(self):
        print("Kucing {} dengan usia {} bulan".format(self.usia, self.warna))

kucing1 = kucing(8, "coklat")
kucing1.mengeong()
