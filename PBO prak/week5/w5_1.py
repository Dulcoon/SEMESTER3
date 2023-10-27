class UTY:
  def __init__(self, id, nama, alamat):
    self._id = id
    self.nama = nama
    self.alamat = alamat

  def perkenalan(self):
    print("Halo, nama saya", self.nama, "saya tinggal di", self.alamat)

class Student(UTY):
  def __init__(self, id, nama, alamat, prodi, angkatan, ipk):
    super().__init__(id, nama, alamat)
    self.prodi = prodi
    self.angkatan = angkatan
    self.__ipk = ipk

  # method setter getter untuk validasi angkatan
  @property
  def angkatan(self):
    return self._angkatan

  @angkatan.setter
  def angkatan(self, angkatan):
    if angkatan < 2017:
      self._angkatan = 2017
    elif angkatan > 2023:
      self._angkatan = 2023
    else:
      self._angkatan = angkatan


    # method untuk student
  def perkenalan_student(self):
    self.perkenalan()
    print("Saya mahasiswa prodi", self.prodi, "angkatan", self.angkatan,)

  def perkenalan_privat_student(self):
    self.perkenalan()
    print("IPK saya", self.__ipk)

class Dosen(UTY):
  def __init__(self, id, nama, alamat, homebase, keahlian, gaji):
    super().__init__(id, nama, alamat)
    self.homebase = homebase
    self.keahlian = keahlian
    self.__gaji = gaji

class Tendik(UTY):
  def __init__(self, id, nama, alamat, unitkerja, gaji):
    super().__init__(id, nama, alamat)
    self.unitkerja = unitkerja
    self.__gaji = gaji