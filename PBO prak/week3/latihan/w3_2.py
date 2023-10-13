class DataIbu:
    def __init__(self, nama, usia, pekerjaan):
        self.nama = nama
        self.usia = usia
        self.pekerjaan = pekerjaan
    def cetakDataIbu(self):
        print("====== Data Ibu ======")
        print("Nama Ibu :",self.nama)
        print("Usia Ibu :",self.usia)
        print("Pekerjaan Ibu :",self.pekerjaan)

class Nilai:
    def __init__(self, pbo, web, sistem_digital):
        self.pbo = pbo
        self.web = web
        self.sistem_digital = sistem_digital
    def cetakDataNilai(self):
        print("====== Data Nilai ======")
        print("Nilai PBO :",self.pbo)
        print("Nilai Pemrograman Web :",self.web)
        print("Nilai Sistem Digital :",self.sistem_digital)
