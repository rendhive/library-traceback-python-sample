import traceback

try:
    1 / 0  # Ini akan menimbulkan ZeroDivisionError
except ZeroDivisionError:
    traceback.print_exc()
# Fungsi: Menangani dan mencetak jejak proses error saat terjadi exception.
# Kondisi: Ketika Anda ingin mendapatkan detail tentang kesalahan.