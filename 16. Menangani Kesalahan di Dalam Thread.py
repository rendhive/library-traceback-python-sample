import logging
import traceback
import threading

def thread_function():
    raise RuntimeError("Runtime Error dalam Thread")

def handle_thread():
    try:
        thread_function()
    except RuntimeError:
        logging.error("Error dari thread:\n%s", traceback.format_exc())

# Menjalankan thread
thread = threading.Thread(target=handle_thread)
thread.start()
thread.join()
# Fungsi: Menangani kesalahan yang terjadi dalam thread menggunakan traceback.
# Kondisi: Ketika Anda ingin menangkap kesalahan yang muncul di thread yang berbeda.