def binarysearch(arr, target):
    # cek jika yg diinput adalah ganjil
    if target % 2 != 0:
        print(f"Nilai {target} adalah angka ganjil dan tidak bisa ditemukan.")
        return -1
    
    # batas bawah dan atas
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        # jika yang dicari adalah nilai tengah, kembalikan indeksnya
        if arr[mid] == target:
            return mid
        # jika yang dicari lebih kecil dari nilai tengah, fokus pada bagian kiri
        elif arr[mid] > target:
            high = mid - 1
        # jika yg dicari lebih besar, fokus pada bagian kanan
        else:
            low = mid + 1
    
    # jika tidak ditemukan, kembalikan -1
    return -1

# list angka genap 
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# input user
target = int(input("Masukkan angka yang ingin dicari: "))

# memanggil fungsi binary
result = binarysearch(arr, target)

# hasil
if result != -1:
    print(f"Nilai {target} ditemukan pada indeks {result}.")
else:
    if target % 2 == 0:
        print(f"Nilai {target} tidak ditemukan di dalam list.")
