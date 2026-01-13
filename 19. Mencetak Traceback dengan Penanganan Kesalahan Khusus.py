import traceback

try:
    10 / 0
except ZeroDivisionError:
    print("Kesalahan telah terjadi:")
    tb_str = traceback.format_exc()
    print("Traceback detail:\n", tb_str)
# Fungsi: Menangani kesalahan dengan detail yang lebih komprehensif.
# Kondisi: Ketika Anda ingin memberikan rincian yang lebih tepat mengenai kesalahan.