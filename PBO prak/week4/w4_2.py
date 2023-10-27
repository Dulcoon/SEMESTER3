class Mahasiswa:
    def __init__(self):
        self.nama = None
        self.alamat = None
        self._umur = 0


    # membuat function getter menggunakan property decorator
    @property
    def umur(self):
        print("Method Getter dipanggil untuk atribut umur")
        return self._umur

    # membuat method setter
    @umur.setter
    def umur(self, a):
        if(a<18):
            print("Maaf anda blm boleh menonton")
        else:
            print("Silahkan")
        print("Method setter untuk atribut umur dipanggil")
        self._umur = a

bejo = Mahasiswa()
bejo.umur=15
bejo.nama = "Andi"
bejo.alamat = "Sleman"
print(bejo.nama)
print(bejo.alamat)
print(bejo.umur)

# print(bejo._umur)