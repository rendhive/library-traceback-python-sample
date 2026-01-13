import traceback

class CustomError(Exception):
    pass

def function_with_custom_error():
    raise CustomError("Ini adalah kesalahan kustom")

try:
    function_with_custom_error()
except CustomError:
    traceback.print_exc()
# Fungsi: Menangani kesalahan dengan exception kustom dan mencetak jejaknya.
# Kondisi: Ketika Anda bekerja dengan exception yang didefinisikan sendiri.