import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung total dan menampilkan hasil
def hitung_total():
    try:
        # Mengambil input dari Entry
        menu_makanan = int(entry_makanan.get())
        Jumlah_porsi = int(entry_porsi.get())
        menu_minuman = int(entry_minuman.get())
        Jumlah_gelas = int(entry_gelas.get())

        # Menghitung total makanan
        if menu_makanan == 1:
            total_makanan = Jumlah_porsi * 12000
            nama_makanan = "Nasi Goreng"
        elif menu_makanan == 2:
            total_makanan = Jumlah_porsi * 12000
            nama_makanan = "Ayam Goreng"
        elif menu_makanan == 3:
            total_makanan = Jumlah_porsi * 5000
            nama_makanan = "Mie Goreng/Rebus"
        elif menu_makanan == 4:
            total_makanan = Jumlah_porsi * 2000
            nama_makanan = "Ketoprak"
        elif menu_makanan == 5:
            total_makanan = Jumlah_porsi * 20000
            nama_makanan = "Ikan Bakar"
        else:
            messagebox.showerror("Error", "Pilihan makanan tidak tersedia")
            return
        
        # Menghitung total minuman
        if menu_minuman == 1:
            total_minuman = Jumlah_gelas * 4000
            nama_minuman = "Es Teh"
        elif menu_minuman == 2:
            total_minuman = Jumlah_gelas * 4000
            nama_minuman = "Es Jeruk"
        elif menu_minuman == 3:
            total_minuman = Jumlah_gelas * 5000
            nama_minuman = "Soda Gembira"
        elif menu_minuman == 4:
            total_minuman = Jumlah_gelas * 5000
            nama_minuman = "Kopi Susu"
        else:
            messagebox.showerror("Error", "Pilihan minuman tidak tersedia")
            return
        
        # Menghitung total seluruhnya
        jumlah_semuanya = total_makanan + total_minuman

        # Menampilkan hasil
        result = (f"Makanan : {nama_makanan}\n"
                  f"Porsi   : {Jumlah_porsi}\n"
                  f"Minuman : {nama_minuman}\n"
                  f"Gelas   : {Jumlah_gelas}\n"
                  f"\nTotal Harga : Rp. {jumlah_semuanya}")
        messagebox.showinfo("Daftar Pembelian", result)
    
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid")

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Program Kasir Sederhana")

# Label dan Entry untuk input makanan
tk.Label(root, text="Pilih Makanan (1-5)").pack()
entry_makanan = tk.Entry(root)
entry_makanan.pack()

# Label dan Entry untuk input jumlah porsi
tk.Label(root, text="Jumlah Porsi").pack()
entry_porsi = tk.Entry(root)
entry_porsi.pack()

# Label dan Entry untuk input minuman
tk.Label(root, text="Pilih Minuman (1-4)").pack()
entry_minuman = tk.Entry(root)
entry_minuman.pack()

# Label dan Entry untuk input jumlah gelas
tk.Label(root, text="Jumlah Gelas").pack()
entry_gelas = tk.Entry(root)
entry_gelas.pack()

# Tombol untuk menghitung total dan menampilkan hasil
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack()

# Menjalankan aplikasi
root.mainloop()
