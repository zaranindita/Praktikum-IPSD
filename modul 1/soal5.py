
import random
def tebakangka():
    angkarahasia = random.randint(1, 100) 
    kesempatan = 5  

    print("Selamat datang di permainan tebak angka!")
    print("Pilih angka antara 1 hingga 100.")
    print(f"Kamu punya {kesempatan} kesempatan untuk menebaknya.\n")

    for percobaan in range(1, kesempatan + 1):
        try:
            tebakan = int(input(f"Tebakan {percobaan}: Masukkan angka: "))

            if tebakan < 1 or tebakan > 100:
                print("Angka harus antara 1 dan 100! Coba lagi.\n")
                continue

            if tebakan == angkarahasia:
                print(f"Selamat! Kamu menebak angka yang benar ({angkarahasia}) dalam {percobaan} percobaan.")
                break
            elif tebakan < angkarahasia:
                print("Tebakanmu terlalu kecil.")
            else:
                print("Tebakanmu terlalu besar.")
            
            if percobaan == kesempatan:
                print(f"kamu kehabisan kesempatan! angka yang benar adalah {angkarahasia}.")

        except ValueError:
            print("Harap masukkan angka yang valid!")

if __name__ == "__main__":
    tebakangka()
