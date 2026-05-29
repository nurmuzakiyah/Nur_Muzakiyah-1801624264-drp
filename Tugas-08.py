user = input ("Masukan Namamu Disini!")

print (f"\n ✨ 1. Papan Catur Input Tugas {user}✨")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print ("⬛", end=" ")
        else:
            print ("⬜", end=" ")
    print()

print(f"\n ✨ 2. Daftar Tugas {user}✨")

Daftar_tugas = []
Jumlah_tugas = int(input("Berapa Banyak Tugas yang Ingin Kamu Lakukan? "))

for i in range(Jumlah_tugas):
    print()
    print(f"\n✨Tugas ke-{i+1}✨")

    Nama_tugas = input("Nama tugas: ")
    Bentuk_tugas = input("Bentuk tugas: ")
    Pengerjaan_tugas = input("Pengerjaan tugas: ")
    Tenggat_tugas = input("Tenggat tugas: ")

    Tugas= {
        "Tugas": Nama_tugas,
        "Bentuk": Bentuk_tugas,
        "Pengerjaan": Pengerjaan_tugas,
        "Tenggat": Tenggat_tugas
    }
    Daftar_tugas.append (Tugas)
print()

print(f"\n✨Daftar Tugas yang sudah {user} masukkan✨")

for i in range(len(Daftar_tugas)):
    print(f"Tugas {i + 1}")
    print(f"Nama tugas: {Daftar_tugas[i]['Tugas']}")
    print(f"Bentuk tugas: {Daftar_tugas[i]['Bentuk']}")
    print(f"Pengerjaan tugas: {Daftar_tugas[i]['Pengerjaan']}")
    print(f"Tenggat tugas: {Daftar_tugas[i]['Tenggat']}")
    print()