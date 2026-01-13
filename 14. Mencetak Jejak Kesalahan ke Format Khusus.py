import traceback

def risky():
    return 5 / 0

try:
    risky()
except ZeroDivisionError:
    tb_str = traceback.format_exc()
    print("Custom formatted traceback:\n", tb_str.strip())
# Fungsi: Mencetak jejak kesalahan dalam format yang diatur.
# Kondisi: Ketika Anda ingin menampilkan jejak kesalahan dengan cara yang spesifik.