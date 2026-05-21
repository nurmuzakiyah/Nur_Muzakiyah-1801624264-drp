from datetime import datetime 

print("Halo!")
print("Silahkan dipilih!")
print("sarapan")
print("pergi kerja")

aktivitas = input("Pilih aktivitas yang kamu ingin lakukan sekarang:")

if aktivitas.lower() == "sarapan":

    print("Ini pilihan menu makanannya, silahkan dipilih ya!")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("Mau sarapan dengan menu apa?")

    if menu.lower () == "telur" or menu.lower () == "ikan" or menu.lower() == "nugget":
        print (f"OK, {menu} tersedia. Silahkan memasaknya terlebih dahulu ya!")
    else:
        print (f"Yah bahannya tidak ada, yuk kita beli dulu!")

elif aktivitas.lower () == "pergi kerja":
    waktu = datetime.now()
    print("waktu kamu pergi kerja, jam 08.00 pagi ya!")
    print (f"sudah saatnya {waktu}")

    if waktu.hour < 08.00:
        print ("wah, masih banyak waktu tersisa, bersiap dan sarapan terlebih dahulu ya!")
    elif waktu.hour == 08.00:
        print ("waktu sudah menunjukkan pukul 08.00, yuk waktunya pergi kerja!")
    else:
        print("wah, kamu sudah terlambat, pasang alarm mu dan bangun lebih pagi besok ya!")