import logging
import traceback

# Mengatur logger
logging.basicConfig(filename='traceback.log', level=logging.ERROR)

try:
    1/0
except ZeroDivisionError:
    logging.error("Jejak Kesalahan:\n%s", traceback.format_exc())
# Fungsi: Menyimpan jejak kesalahan ke dalam file log.
# Kondisi: Ketika Anda ingin melakukan pencatatan kesalahan untuk tujuan audit.