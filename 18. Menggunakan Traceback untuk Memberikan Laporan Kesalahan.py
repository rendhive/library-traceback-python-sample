import traceback

def perform_task():
    """Melaksanakan tugas yang mungkin gagal."""
    return "result"

try:
    perform_task()
    raise ValueError("Contoh kesalahan")
except Exception:
    print("Laporan kesalahan:")
    traceback.print_exc()
# Fungsi: Menyajikan laporan kesalahan saat terjadi kesalahan di dalam fungsi.
# Kondisi: Ketika Anda ingin melapor kesalahan ke sistem atau ke pengguna.