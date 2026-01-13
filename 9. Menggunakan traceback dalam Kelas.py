import traceback

class MyClass:
    def method(self):
        return 5 / 0

try:
    obj = MyClass()
    obj.method()
except Exception:
    print("Error in MyClass method:")
    traceback.print_exc()
# Fungsi: Mengelola kesalahan dalam metode kelas.
# Kondisi: Ketika Anda perlu mengetahui kesalahan dalam implementasi objek.