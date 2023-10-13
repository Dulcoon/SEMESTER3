# Mihael Valensio One Febian
# 5220411200

from w3_1 import *
from w3_2 import *
from w3_3 import *
import os

data1 = False
data2 = False
data3 = False
data4 = False
while True:
    print("=" * 30)
    print("1. Isi data Pribadi Mahasisawa")
    print("2. Isi Nilai Mahasisawa")
    print("3. Isi data Orang Tua Mahasiswa (Ayah) : ")
    print("4. Isi data Orang Tua Mahasiswa (Ibu)")
    print("5. Cetak Data mahasiswa : ")
    print("0. Keluar : ")
    print("=" * 30)
    menu = int(input("Masukkan Menu : "))
    if(menu>5) or (menu<0):
        print("Menu yang anda pilih salah, perhatikan menu yang tersedia, silahkan run ulang!")
        break
    elif menu == 1:
        nama = input("Masukkan Nama Mhs : ")
        npm = input("Masukkan NPM Mhs : ")
        prodi = input("Masukkan Prodi Mhs : ")
        alamat = input("Masukkan alamat Mhs : ")
        data1 = True
        print("selesai input")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 2:
        pbo = input("Masukkan Nilai PBO : ")
        web = input("Masukkan Nilai Pemrograman Web : ")
        sisdig = input("Masukkan Nilai Sistem Digital : ")
        data2 = True
        print("selesai input")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 3:
        namaAyah = input("Masukkan nama ayah : ")
        usiaAyah = input("Masukkan Usia ayah : ")
        pekerjaanAyah = input("Masukkan Pekerjaan Ayah ")
        data3 = True
        print("selesai input")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 4:
        namaIbu = input("Masukkan nama Ibu : ")
        usiaIbu = input("Masukkan Usia Ibu : ")
        pekerjaanIbu = input("Masukkan Pekerjaan Ibu ")
        data4 = True
        print("selesai input")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 5:
        if (data1 and data2 and data3 and data4 == True):
            mhs1 = Mahasiswa(nama, npm ,prodi, alamat)
            mhs1.cetakDataMhs()
            nilaiMhs = Nilai(pbo,web,sisdig)
            nilaiMhs.cetakDataNilai()
            ayahMhs = DataAyah(namaAyah,usiaAyah,pekerjaanAyah)
            ayahMhs.cetakDataAyah()
            ayahMhs = DataIbu(namaIbu,usiaIbu,pekerjaanIbu)
            ayahMhs.cetakDataIbu()
        else:
            print("Pastikan semua data telah terisi!")
        input("[Pres ENTER To Continue]")
        os.system("cls")
    elif menu == 0:
        print("Terimakasih")
        break


