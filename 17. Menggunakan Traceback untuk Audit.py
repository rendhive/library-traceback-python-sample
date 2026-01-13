import traceback

def faulty_operation():
    return 1 / 0

try:
    faulty_operation()
except Exception:
    print("Audit jejak kesalahan:")
    print(traceback.format_exc())
# Fungsi: Mencetak jejak kesalahan untuk tujuan audit.
# Kondisi: Ketika Anda ingin menyimpan atau memeriksa jejak kesalahan untuk keperluan compliance atau audit.