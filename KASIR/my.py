# Fungsi untuk daftar makanan
def makanan():
    global total_makanan, Jumlah_porsi, nama_makanan

# Fungsi untuk daftar minuman
def minuman():
    global total_minuman, Jumlah_gelas, nama_minuman

print("|------------------------------|")
print("| Program Mesin Kasir Sederhana|")
print("|------------------------------|")
print("|      Pilih Menu Makanan      |")
print("|------------------------------|")
print("| 1. Nasi Goreng      Rp. 12000|")
print("| 2. Ayam Goreng      Rp. 12000|")
print("| 3. Mie Goreng/Rebus Rp.  5000|")
print("| 4. Ketoprak         Rp.  2000|")
print("| 5. Ikan Bakar       Rp. 20000|")
print("|------------------------------|")
menu_makanan = int(input("Pilih Makanan (1/2/3/4/5) : "))
Jumlah_porsi = int(input("Jumlah Makanan :  "))

if menu_makanan == 1 :
    total_makanan = Jumlah_porsi * 12000
    print(" Nasi Goreng", Jumlah_porsi, "Porsi : Rp.  ", total_makanan)
    nama_makanan = "Nasi Goreng"
elif menu_makanan == 2:
    total_makanan = Jumlah_porsi * 12000
    print(" Ayam Goreng", Jumlah_porsi, "Porsi : Rp.  ", total_makanan)
    nama_makanan = "Ayam Goreng"
elif menu_makanan == 3:
    total_makanan = Jumlah_porsi * 5000
    print(" Mie Goreng/Rebus", Jumlah_porsi, "Porsi : Rp.  ", total_makanan)
    nama_makanan = "Mie Goreng/Rebus"
elif menu_makanan == 4:
    total_makanan = Jumlah_porsi * 2000
    print(" Ketoprak", Jumlah_porsi, "Porsi : Rp.  ", total_makanan)
    nama_makanan = "Ketoprak"
elif menu_makanan == 5:
    total_makanan = Jumlah_porsi * 20000
    print(" Ikan Bakar", Jumlah_porsi, "Porsi : Rp.  ", total_makanan)
    nama_makanan = "Ikan Bakar"
else:
    print("Pilihan Tidak Tersedia")
    total_makanan = 0
    nama_makanan = "Tidak ada"

print()
print("|------------------------------|")
print("|      Pilih Menu Minuman      |")
print("|------------------------------|")
print("| 1. Es Teh           Rp.  4000|")
print("| 2. Es Jeruk         Rp.  4000|")
print("| 3. Soda Gembira     Rp.  5000|")
print("| 4. Kopi Susu        Rp.  5000|")
print("|------------------------------|")
menu_minuman = int(input("Pilih Minuman (1/2/3/4) : "))
Jumlah_gelas = int(input("Jumlah Gelas :  "))

if menu_minuman == 1:
    total_minuman = Jumlah_gelas * 4000
    print(" Es Teh", Jumlah_gelas, "Gelas : Rp.  ", total_minuman)
    nama_minuman = "Es Teh"
elif menu_minuman == 2:
    total_minuman = Jumlah_gelas * 4000
    print(" Es Jeruk", Jumlah_gelas, "Gelas : Rp.  ", total_minuman)
    nama_minuman = "Es Jeruk"
elif menu_minuman == 3:
    total_minuman = Jumlah_gelas * 5000
    print(" Soda Gembira", Jumlah_gelas, "Gelas : Rp.  ", total_minuman)
    nama_minuman = "Soda Gembira"
elif menu_minuman == 4:
    total_minuman = Jumlah_gelas * 5000
    print(" Kopi Susu", Jumlah_gelas, "Gelas : Rp.  ", total_minuman)
    nama_minuman = "Kopi Susu"
else:
    print("Pilihan Tidak Tersedia")
    total_minuman = 0
    nama_minuman = "Tidak ada"

# Proses Menghitung Semua Harga Yang Harus Dibayar
makanan()
minuman()
jumlah_semuanya = total_makanan + total_minuman

# Daftar Pembelian
print()
print("|===================================|")
print("|        DAFTAR PEMBELIAN           |")
print("|===================================|")
print("|Makanan : ", nama_makanan,"\t     |")
print("|Porsi   :  ", Jumlah_porsi,"\t\t\t|")
print("|Minuman : ", nama_minuman,"\t     |")
print("|Gelas   : ", Jumlah_gelas,"\t\t\t |")
print("|===================================|")
print("|   JUMLAH YANG HARUS DIBAYAR       |")
print("|===================================|")
print("|Total : Rp.", jumlah_semuanya,"   |")
print("|===================================|")