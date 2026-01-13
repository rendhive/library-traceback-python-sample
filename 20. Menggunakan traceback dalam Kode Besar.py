import traceback

def main_function():
    try:
        process_data()
    except Exception:
        print("Error in main function:")
        traceback.print_exc()

def process_data():
    raise RuntimeError("Kesalahan terjadi saat memproses data")

# Menjalankan fungsi utama
main_function()
# Fungsi: Menangani kesalahan dalam fungsi utama menggunakan traceback untuk pelacakan.
# Kondisi: Ketika Anda bekerja dengan alur kode yang lebih rumit dan ingin melacak kesalahan dengan rinci.