import traceback

try:
    "string" + 1  # Ini akan menimbulkan TypeError
except TypeError:
    error_message = traceback.format_exc()
    print(error_message)
# Fungsi: Mengambil jejak error sebagai string.
# Kondisi: Ketika Anda perlu menyimpan atau memproses jejak error.