class Mahasiswa:
    def __init__(self, nim, nama, prodi, ipk, uangSaku) :
        self._nim = nim
        self.nama = nama
        self.prodi = prodi
        self.__ipk = ipk
        self._uangSaku = uangSaku

    def publicPerkenalan(self):
        print("Perkenalkan nama saya", self.nama, "kuliah di prodi", self.prodi)

    def _protected_nim_dan_uang_saku(self):
        print("Ini ranah khusus keluarga dan teman")
        print("Nama saya              :",self.nama)
        print("NIM saya di Prodi      :", self.prodi, "Adalah",self._nim)
        print("Uang saku saya per bulan Rp", self._uangSaku)

    def __privat_IPK(self):
        print("Ini Ranah privat saya")
        print("Nama saya", self.nama, "IPK saya",self.__ipk)

    def aksesPrivat(self):
        self.__privat_IPK()

    def aksesProtected(self):
        self._protected_nim_dan_uang_saku()

nim = input("Masukkan NIM :")
nama = input("Masukkan Nama :")
prodi = input("Masukkan Prodi :")
ipk = float(input("Masukkan IPK :"))
saku = int(input("Masukkan Uang saku per bulan : "))

mhs1 = Mahasiswa(nim, nama, prodi, ipk, saku)

print("Akses method public")
mhs1.publicPerkenalan()

print("Akses method protected")
mhs1._protected_nim_dan_uang_saku()

print("Akses method Privat")
mhs1.aksesPrivat()
