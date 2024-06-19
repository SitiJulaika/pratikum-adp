import time
import os
from termcolor import cprint, colored
os.system('cls')

print("PROJEK UAS ADP PROGRAM TOKO ALAT TULIS")
print('Nama/NIM : Selfi Olivia/2310431033')
print('Nama/NIM : Siti Julaika/2310432031')
print()
print("  =====================================")
print("          SELAMAT DATANG DI TOKO")
print("                 SELARAS ")
print("            -TOKO ALAT TULIS-")
print("  =====================================")
print()
print("Eh, keranjang belanja kamu masih kosong :(")
print("Boleh dong, dipilih dulu alat tulisnya!")
print()

menu = [
    ["Pensil", 2000],
    ["Pulpen", 3000],
    ["Buku Tulis", 5000],
    ["Penghapus", 1500],
    ["Penggaris", 2500]
]

barang = 0
pesanan = []
struk = []
print()

def tampilkan_menu(menu):
    print()
    cprint('>        Menu Alat Tulis Selaras        <', 'black', 'on_white')
    print()
    print("  +------------------------------------+")
    print("  | NO |   JENIS ALAT TULIS   |  HARGA |")
    print("  +------------------------------------+")
    for i in range(len(menu)):
        print(f"  | {i+1}. | {menu[i][0]:18} = Rp {menu[i][1]:>5} |")
    print("  +------------------------------------+")
tampilkan_menu(menu)

def tampilkan_promo(promo):
    for i in range(3):
        print("\r" + " " * len(promo), end="")
        time.sleep(0.3)
        print("\r" + promo, end="")
        time.sleep(0.3)
    print()
promo = "!!! SPESIAL PROMO !!!"
tampilkan_promo(promo)
print("Untuk total pembelian lebih dari Rp 100.000, kamu akan mendapat DISKON 10%")
print()

# Fungsi untuk menulis struk ke file teks
def tulis_struk(struk):
    with open("struk_belanja.txt", "w") as file:
        for item in struk:
            file.write(item + "\n")

def animasi_menghitung():
    animasi = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        print("\rWait A Minute " + animasi[i % len(animasi)], end='')
    print()

mau_pesan = input("Apakah kamu ingin memesan (y/n) ? ").lower()

while mau_pesan not in ["y", "n"]:
    print("Note : silakan masukkan Y/y = yes dan N/n = no !")
    mau_pesan = input("Apakah kamu ingin memesan (y/n) ? ").lower()

if mau_pesan == "y":
    while mau_pesan == "y":
        jenis = int(input("Tulis nomor jenis alat tulis yang ingin kamu beli : "))
        jumlah = int(input(f"Jumlah yang ingin dipesan untuk jenis alat tulis nomor {jenis}: "))
        
        if 1 <= jenis <= len(menu):
            harga = jumlah * menu[jenis - 1][1]
            pesanan.append((menu[jenis - 1][0], jumlah, harga))
        else:
            print("Yah, Jenis alat tulis yang kamu masukkan tidak tersedia nih!")
            break

        barang += harga
        mau_pesan = input("Apakah kamu ingin memesan lagi (y/n) ? ").lower()

def hitung_diskon(total):
    if total > 100000:  
        return total * 0.1
    else:
        return 0

diskon_total = hitung_diskon(barang)
barang_akhir = barang - diskon_total

if barang == 0:
    print("Kamu tidak memesan alat tulis apapun.")

for item in pesanan:
    struk.append(f"{item[0]:<12}|{item[1]:<12}  |Rp {item[2]:<12}")
if diskon_total > 0:
    struk.append(f"TOTAL               :     Rp {int(barang):<12}")
    struk.append(f"DISKON 10%          :     Rp -{int(diskon_total):<12}")
struk.append(f"TOTAL HARGA :     Rp {int(barang_akhir):<12}")

print()
tulis_struk(struk)
animasi_menghitung()
print()

print("  ==================================================")
print("                 STRUK BELANJA CUSTOMER")
print("                     TOKO SELARAS")
print("                   -TOKO ALAT TULIS-")
print("  ==================================================")
print()
for item in struk:
    print("    " + item)
print()
print("  ==================================================")
print("       TERIMAKASIH TELAH BERBELANJA DI SELARAS")
cprint("            -ENJOY YOUR ACTIVITIES-                 ",'black','on_white')