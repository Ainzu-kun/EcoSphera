import pandas as pd
import os



# File paths
DATA_FILE = "banksampah.csv"
SAMPAH_FILE = "datasampah.csv"

# Load or initialize data
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["ID", "Nama Bank Sampah", "Nama Pengelola", "Lokasi", "Kontak Pengelola"]).to_csv(DATA_FILE, index=False)

if not os.path.exists(SAMPAH_FILE):
    pd.DataFrame(columns=["Jenis Sampah", "Berat"]).to_csv(SAMPAH_FILE, index=False)

def load_data():
    df = pd.read_csv(DATA_FILE)
    if "ID" not in df.columns:
        df.insert(0, "ID", range(1, len(df) + 1))  # Tambahkan kolom ID jika belum ada
        save_data(df)
    return df

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def create_entry():
    df = load_data()
    nama_bank = input("Masukkan Nama Bank Sampah: ")
    nama_pengelola = input("Masukkan Nama Pengelola: ")
    lokasi = input("Masukkan Lokasi: ")
    kontak_pengelola = input("Masukkan Kontak Pengelola: ")
    
    new_id = df["ID"].max() + 1 if not df.empty else 1
    new_entry = pd.DataFrame({"ID": [new_id], "Nama Bank Sampah": [nama_bank], "Nama Pengelola": [nama_pengelola], 
                              "Lokasi": [lokasi], "Kontak Pengelola": [kontak_pengelola]})
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    print("Data Sukses Ditambahkan")

def read_entries():
    df = load_data()
    if df.empty:
        print("Belum ada data bank sampah.")
    else:
        print(df)

def update_entry():
    df = load_data()
    print("\n=== Perbarui Data ===")
    print(df)

    id_ = input("Masukkan ID yang ingin diubah: ")
    if not id_.isdigit() or int(id_) not in df["ID"].values:
        print("ID tidak ditemukan!")
        return

    id_ = int(id_)
    print("Data saat ini:")
    print(df[df["ID"] == id_])

    nama_bank = input("Masukkan Nama Bank Sampah Baru (biarkan kosong jika tidak diubah): ")
    nama = input("Masukkan Nama Pengelola Baru (biarkan kosong jika tidak diubah): ")
    lokasi = input("Masukkan Lokasi Baru (biarkan kosong jika tidak diubah): ")
    kontak = input("Masukkan Kontak Pengelola Baru (biarkan kosong jika tidak diubah): ")

    if nama_bank:
        df.loc[df["ID"] == id_, "Nama Bank Sampah"] = nama_bank
    if nama:
        df.loc[df["ID"] == id_, "Nama Pengelola"] = nama
    if lokasi:
        df.loc[df["ID"] == id_, "Lokasi"] = lokasi
    if kontak:
        df.loc[df["ID"] == id_, "Kontak Pengelola"] = kontak
    save_data(df)
    print("Data berhasil diperbarui!")

def delete_entry():
    df = load_data()
    print("\n=== Hapus Data ===")
    print(df)

    id_ = input("Masukkan ID yang ingin dihapus: ")
    if not id_.isdigit() or int(id_) not in df["ID"].values:
        print("ID tidak ditemukan!")
        return

    id_ = int(id_)
    df = df[df["ID"] != id_]  # Hapus baris dengan ID yang dimaksud
    save_data(df)
    print("Data berhasil dihapus!")

def main_menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. CRUD Menu")
        print("2. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            crud_menu()
        elif choice == "2":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih menu yang tersedia.")

def crud_menu():
    while True:
        print("\n=== Menu CRUD ===")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Logout")
        choice = input("Pilih menu: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Logout Berhasil")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih menu yang tersedia.")

main_menu()
