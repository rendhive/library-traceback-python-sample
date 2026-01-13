import traceback

def multi_exception():
    try:
        10 / 0
    except ZeroDivisionError:
        traceback.print_exc()
    try:
        'a' + 1
    except TypeError:
        traceback.print_exc()

multi_exception()
# Fungsi: Menangani beberapa jenis exception dalam satu fungsi.
# Kondisi: Ketika Anda ingin menentukan dan mencetak jejak untuk beberapa kesalahan sekaligus.