import traceback

def another_function():
    raise ValueError("Nilai tidak valid")

def main_function():
    try:
        another_function()
    except ValueError:
        print("Jejak Stack:")
        traceback.print_stack()
# Menjalankan uji
main_function()
# Fungsi: Mencetak jejak stack saat kesalahan terjadi dalam nested function.
# Kondisi: Ketika Anda ingin memeriksa jalur eksekusi saat terjadi kesalahan dalam pengendalian yang lebih dalam.