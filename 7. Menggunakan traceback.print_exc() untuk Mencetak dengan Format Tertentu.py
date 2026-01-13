import traceback

try:
    result = 'abc' - 1  # Ini akan memicu TypeError
except Exception:
    print("An error occurred:")
    traceback.print_exc(limit=1)  # Hanya menunjukkan rincian satu level
# Fungsi: Mencetak jejak kesalahan dengan batasan tertentu.
# Kondisi: Ketika Anda ingin membatasi output jejak kesalahan.