from w5_1 import UTY
from w5_1 import Student
from w5_1 import Dosen
from w5_1 import Tendik
import os

while True:
  os.system("cls")
  print("Menu pilihan")
  print("1. Tambah data mahasiswa")
  print("2. Tambah data dosen")
  print("3. Tambah data tendik")
  print("4. Tampilkan data mahasiswa")
  print("5. Tampilkan data dosen")
  print("6. Tampilkan data tendik")
  print("0. Selesai")
  pilih = int(input("Masukkan pilihan anda: "))
  if pilih == 1:
    os.system("cls")
    print("Tambah data mahasiswa")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    prodi = input("Masukkan prodi: ")
    angkatan = input("Masukkan angkatan: ")
    ipk = float(input("Masukkan angkatan: "))
    mhs1 = Student(nim, nama, alamat, prodi, angkatan, ipk)
    mhs1.angkatan = angkatan
    input("Tekan enter untuk kembali ke menu")
  elif pilih == 2:
    print("Tambah data dosen")
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    uty = UTY(nik, nama, alamat)
    Dosen.add_dosen(uty)
  elif pilih == 3:
    print("Tambah data tendik")
    nik = input("Masukkan NIK: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    uty = UTY(nik, nama, alamat)
    Tendik.add_tendik(uty)
  elif pilih == 4:
    print("Tampilkan data mahasiswa")
    Student.show_student()
  elif pilih == 5:
    print("Tampilkan data dosen")
    Dosen.show_dosen()
  elif pilih == 6:
    print("Tampilkan data tendik")
    Tendik.show_tendik()
  elif pilih == 0:
    print("Terima kasih")
    break
  else:
    print("Pilihan tidak tersedia")
    input("Tekan enter untuk kembali ke menu")
