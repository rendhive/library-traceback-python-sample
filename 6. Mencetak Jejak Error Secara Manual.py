import traceback

try:
    10 / 0
except Exception:
    print("Manual traceback:")
    tb = traceback.extract_stack()
    print(traceback.format_list(tb))
# Fungsi: Menampilkan jejak stack secara manual.
# Kondisi: Ketika Anda ingin tahu bagaimana kode mencapai keadaan saat ini.