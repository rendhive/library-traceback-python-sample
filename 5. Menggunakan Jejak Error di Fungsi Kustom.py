import traceback

def risky_function():
    return 1 / 0

try:
    risky_function()
except ZeroDivisionError as e:
    print("Error detected:")
    traceback.print_exc()
# Fungsi: Menangani kesalahan dalam fungsi dan mencetak jejak kesalahan.
# Kondisi: Ketika Anda ingin menelusuri kesalahan dalam pemanggilan fungsi.