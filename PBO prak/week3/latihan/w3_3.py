class Mahasiswa:
    def __init__(self, nama, npm, prodi, alamat):
        self.nama = nama
        self.npm = npm
        self.prodi = prodi
        self.alamat = alamat
        
    def cetakDataMhs(self):
        print("====== Data Pribadi Mahasiswa ======")
        print("Nama Mhs :",self.nama)
        print("NPM :",self.npm)
        print("Prodi :",self.prodi)
        print("Alamat :",self.alamat)