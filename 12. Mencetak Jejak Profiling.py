import traceback

def faulty_function():
    return 10 / 0

def wrapper_function():
    try:
        faulty_function()
    except ZeroDivisionError:
        traceback.print_exc()
    
wrapper_function()
# Fungsi: Menggunakan traceback untuk mencetak jejak kesalahan di lingkungan yang rumit.
# Kondisi: Ketika Anda perlu mengetahui jejak kesalahan dengan auditan lebih dalam.