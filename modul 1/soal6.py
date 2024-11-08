
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def urutanfaktorial(n):
    hasil = []
    for i in range(n + 1):
        hasil.append(faktorial(i))
    return hasil

# main
n = int(input("Masukkan bilangan bulat n: "))
output = urutanfaktorial(n)
print("Output:", ', '.join(map(str, output)))
