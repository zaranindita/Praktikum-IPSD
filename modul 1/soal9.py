
from datetime import datetime
class buku:
    def __init__(buku, judul, penulis, tahun_terbit):
        buku.judul = judul
        buku.penulis = penulis
        buku.tahun_terbit = tahun_terbit

    # informasi buku
    def tampilkan_informasi(buku):
        print(f"Judul: {buku.judul}")
        print(f"Penulis: {buku.penulis}")
        print(f"Tahun Terbit: {buku.tahun_terbit}")

    # usia buku
    def hitung_usia(buku):
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - buku.tahun_terbit
        return usia


# objek buku
buku1 = buku("Pride And Prejudice", "Jane Austin", 1813)
buku2 = buku("Hamlet", "William Shakespare", 1623)
buku3 = buku("Anna Karenina", "Leo Tolstoy", 1873)

# menampilkan informasi dan usia buku
print("Informasi Buku 1:")
buku1.tampilkan_informasi()
print(f"Usia Buku: {buku1.hitung_usia()} tahun\n")

print("Informasi Buku 2:")
buku2.tampilkan_informasi()
print(f"Usia Buku: {buku2.hitung_usia()} tahun\n")

print("Informasi Buku 3:")
buku3.tampilkan_informasi()
print(f"Usia Buku: {buku3.hitung_usia()} tahun")
