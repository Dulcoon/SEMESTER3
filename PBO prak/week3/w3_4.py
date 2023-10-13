from w3_1 import *
from w3_2 import *
from w3_3 import *


while True:
    print("=" * 30)
    print("1. Isi data Mahasisawa")
    print("2. Cetak data Mahasisawa")
    print("3. Isi data Kucing : ")
    print("4. Cetak data Kucing")
    print("5. Isi data Mobil : ")
    print("6. Cetak data Mobil : ")
    print("0. Keluar : ")
    print("=" * 30)
    menu = int(input("Masukkan Menu : "))
    if(menu>6) or (menu<0):
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif menu == 1:
        a = input("NIM ")
        b = input("Nama ")
        c = input("Prodi ")
        d = input("alamat ")
        print("selesai input")
        input("[Pres ENTER To Continue]")
    elif menu == 2:
        mhs1 = mahasiswa(a,b,c,d)
        mhs1.perkenalan()
    elif menu == 3:
        namaKucing = input("Nama ")
        jenisKucing = input("Jenis ")
        print("selesai input")
        input("[Pres ENTER To Continue]")
    elif menu == 4:
        kucing1 = Kucing(namaKucing, jenisKucing)
        kucing1.kenalan()
    elif menu == 5:
        merMobil = input("Merk Mobil ")
        warnaMobil = input("warna ")
        tahunMobil = input("Tahun ")
        print("selesai input")
        input("[Pres ENTER To Continue]")
    elif menu == 6:
        mobil1 = Mobil(merMobil, warnaMobil, tahunMobil)
        mobil1.kelilingKota()


