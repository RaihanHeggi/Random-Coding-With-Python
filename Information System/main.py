import os
import sys

listLaporan = list()


def daftarLaporan():
    while True:
        clear()
        print("======================= Laporan Bencana =========================")
        if len(listLaporan) == 0:
            print("Data Tidak Ada")
        else:
            for x in listLaporan:
                print("===================================")
                print("Nama : " + x[0])
                print("Bencana : " + x[2])
                print("Lokasi : " + x[1])
                print("===================================")
        prompt = input("Ingin Kembali (Y/N) : ")
        if (prompt == "Y") or (prompt == "y"):
            break
    return True


def lihatLaporanLokasi(cabangDamkar):
    clear()
    while True:
        wilayah = input("Masukkan Wilayah Yang Tersedia : ")
        print("======================= Laporan Bencana =========================")
        if len(listLaporan) == 0:
            print("Data Tidak Ada")
        else:
            for x in listLaporan:
                if x[1] == wilayah:
                    print("===================================")
                    print("Nama : " + x[0])
                    print("Bencana : " + x[2])
                    print("Lokasi : " + x[1])
                    print("===================================")
        prompt = input("Ingin Kembali (Y/N) : ")
        if (prompt == "Y") or (prompt == "y"):
            break
    return True


def pelaporanBencana():
    try:
        while True:
            clear()
            print("======================= Pelaporan Bencana =========================")
            print("                        Cabang Damkar                              ")
            for i in range(len(cabangDamkar)):
                print(str(cabangDamkar[i]))
            print("\n")
            nama = input("Silahkan Masukan Nama Anda  : ")
            lokasiKejadian = input("Lokasi Kejadian  : ")
            bencana = input("Bencana Yang Terjadi : ")
            listLaporan.append([nama, lokasiKejadian, bencana])
            prompt = input("Ingin Kembali (Y/N) : ")
            if (prompt == "Y") or (prompt == "y"):
                break
        return True
    except Exception as e:
        print(e)


def main():
    global cabangDamkar
    global clear
    try:
        cabangDamkar = [
            "Kota Bogor",
            "Kab Bogor",
            "Kota Bekasi",
            "Kab Bekasi",
            "Kota Bandung",
            "Cimahi",
        ]
        clear = lambda: os.system("cls")
        clear()
        while True:
            clear()
            print("======================= Menu =========================")
            print(" 1. Pelaporan Bencana")
            print(" 2. Lihat Daftar Laporan Bencana")
            print(" 3. Lihat Daftar Laporan Bencana Per Wilayah")
            print(" 4. Exit")
            prompt = input(" Silahkan Masukan Digit Menu Yang Dipilih : ")
            if prompt == "1":
                pelaporanBencana()
            elif prompt == "2":
                daftarLaporan()
            elif prompt == "3":
                lihatLaporanLokasi(cabangDamkar)
            elif prompt == "4":
                break
            else:
                print("Menu Tidak Ditemukan")
    except Exception as e:
        print(e)


if __name__ == "__main__":

    main()
