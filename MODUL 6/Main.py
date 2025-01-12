class Pegawai:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama  
        self.gaji_pokok = gaji_pokok

    def hitung_lembur(self, jam_lembur, persentase):
        return jam_lembur * (self.gaji_pokok * persentase / 100)

    def hitung_gaji_bersih(self):
        raise NotImplementedError("Subclasses harus mengimplementasikan metode ini")


class PegawaiTetap(Pegawai):
    def __init__(self, nama, gaji_pokok):
        super().__init__(nama, gaji_pokok)

    def hitung_gaji_bersih(self, jam_lembur):
        tunjangan = self.gaji_pokok * 0.7
        lembur = self.hitung_lembur(jam_lembur, 10)
        return self.gaji_pokok + tunjangan + lembur


class PegawaiTidakTetap(Pegawai):
    def __init__(self, nama, gaji_pokok):
        super().__init__(nama, gaji_pokok)

    def hitung_gaji_bersih(self, jam_lembur):
        lembur = self.hitung_lembur(jam_lembur, 5)
        return self.gaji_pokok + lembur


# Contoh Penggunaan
if __name__ == "__main__":
    nama = input("Masukkan nama pegawai: ")
    status = input("Masukkan status pegawai (tetap/tidak tetap): ").lower()
    gaji_pokok = float(input("Masukkan gaji pokok: "))
    jam_lembur = int(input("Masukkan jumlah jam lembur: "))

    if status == "tetap":
        pegawai = PegawaiTetap(nama, gaji_pokok)
    elif status == "tidak tetap":
        pegawai = PegawaiTidakTetap(nama, gaji_pokok)
    else:
        print("Status pegawai tidak valid.")
        exit()

    gaji_bersih = pegawai.hitung_gaji_bersih(jam_lembur)
    print(f"Gaji bersih {pegawai.nama} ({status}): Rp {gaji_bersih:,.2f}")
