import os

class Valen:
    def __init__(self, nama, umur, nik, nohp, tinggiBadan, beratBadan, alamat ):
        self.nama = nama
        self.umur = umur
        self.__nik = nik
        self.__nohp = nohp
        self.__alamat = alamat
        self._tinggiBadan = tinggiBadan
        self._beratBadan = beratBadan
    
    # dataPublic
    def dataPublic(self):
        print("Nama Saya", self.nama)
        print("Umur Saya", self.umur)

    def _protectedDataBadan(self):
        print("Tinggi Badan saya", self._tinggiBadan)
        print("Berat Badan saya", self._beratBadan)

    # dataProtected
    def tampilDataProtected(self):
        self._protectedDataBadan()

    def __privatNim(self):
        print("NPM saya", self.__nik)
        print("IPK saya", self.__nohp)
        print("Saya beralamat di", self.__alamat)
    
    # dataPrivat
    def tampilDataPrivat(self):
        self.__privatNim()

    # Getter untuk tinggiBadan
    @property
    def tinggiBadan(self):
        return self._tinggiBadan

    # Setter untuk tinggiBadan
    @tinggiBadan.setter
    def tinggiBadan(self, new_tinggi):
        self._tinggiBadan = new_tinggi

    # Getter untuk beratBadan
    @property
    def beratBadan(self):
        return self._beratBadan

    # Setter untuk beratBadan
    @beratBadan.setter
    def beratBadan(self, new_berat):
        self._beratBadan = new_berat

while True:
    print("=" * 30)
    print("1. input data")
    print("2. Tampil data Publik")
    print("3. Tampil data Protected : ")
    print("4. Tampil data Privat : ")
    print("5. Edit data Protected : ")
    print("0. Keluar : ")
    print("=" * 30)
    menu = int(input("Masukkan Menu : "))
    if (menu > 5) or (menu < 0):
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif menu == 1:
        nama = input("Masukkan Nama : ")
        umur = input("Masukkan Umur : ")
        nik = input("Masukkan Nomor Induk Kependudukan : ")
        nohp = input("Masukkan Nomor HP : ")
        tinggiBadan = input("Masukkan Tinggi Badan Anda : ")
        beratBadan = input("Masukkan Berat Badan Anda : ")
        alamat = input("Masukkan Alamat Anda : ")
        saya = Valen(nama, umur, nik, nohp, tinggiBadan, beratBadan, alamat)
        print("selesai input")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 2:
        print("====Data Publik Saya====")
        saya.dataPublic()
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 3:
        print("====Data Protected Saya====")
        saya.tampilDataProtected()
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 4:
        print("====Data Privat Saya====")
        saya.tampilDataPrivat()
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 5:
        print("====Edit Data Protected Saya====")
        print("Data saat ini - Tinggi Badan:", saya.tinggiBadan, "Berat Badan:", saya.beratBadan)
        tinggi = input("Masukkan Tinggi Badan Yang Baru : ")
        berat = input("Masukkan Berat Badan Yang Baru : ")
        saya.tinggiBadan = tinggi
        saya.beratBadan = berat
        print("Data Yang Baru Berhasil Diinputkan")
    elif menu == 0:
        print("Terimakasih")
        break