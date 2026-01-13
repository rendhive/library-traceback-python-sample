import traceback

def module_function():
    return 10 / 0

def call_module_function():
    try:
        module_function()
    except Exception:
        print("Error in module function:")
        traceback.print_exc()

call_module_function()
# Fungsi: Menggunakan traceback untuk mengidentifikasi kesalahan dalam fungsi modul.
# Kondisi: Ketika Anda menggunakan fungsi dari modul lain dan ingin melacak kesalahan.