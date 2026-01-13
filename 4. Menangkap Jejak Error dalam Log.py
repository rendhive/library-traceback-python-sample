import logging
import traceback

logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    5 / 0
except ZeroDivisionError:
    logging.error("Terjadi error:\n%s", traceback.format_exc())
# Fungsi: Mencatat jejak error ke dalam file log.
# Kondisi: Ketika Anda ingin menyimpan rincian kesalahan untuk analisis di kemudian hari.