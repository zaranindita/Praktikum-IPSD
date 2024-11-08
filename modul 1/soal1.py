# soal no 1
def bilprima(n):
   # cek apakah n bilangan prima.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prima(hitung):
    # daftar bil prima
    prima = []
    num = 2
    while len(prima) < hitung:
        if bilprima(num):
            prima.append(num)
        num += 1
    return prima

def pola(baris):
    # pola angka
    total_angka = (baris * (baris + 1)) // 2  # angka yang dibutuhkan
    angkaprima = prima(total_angka - 1)  # -1 karena kita mulai dengan 1
    angka = [1] + angkaprima # tamabah 1 diawal

    index = 0
    for i in range(1, baris + 1):
        no_baris = angka[index:index + i]
        print(' '.join(map(str, no_baris)))
        index += i

if __name__ == "__main__":
    barisyangdiinginkan= 4  # jumlah baris
    pola(barisyangdiinginkan)
