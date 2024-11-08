def mincoin(banyak, koin, jumlah):
    # membuat tabel
    dp = [[float('inf')] * (banyak + 1) for _ in range(len(koin) + 1)]
    
    # jika jumlah uang 0, tidak diperlukan koin
    for i in range(len(koin) + 1):
        dp[i][0] = 0
    
    # mengisi tabel
    for i in range(1, len(koin) + 1):
        nilaikoin = koin[i - 1]
        jumlahkoin = jumlah[i - 1]
        
        for j in range(1, banyak + 1):
            # jika tidak pakai koin ke-i
            dp[i][j] = dp[i - 1][j]
            
            # coba pakai koin ke-i sampe batas ketersediaannya
            for k in range(1, jumlahkoin + 1):
                if k * nilaikoin <= j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k * nilaikoin] + k)

    # jika tidak ada solusi, kembalikan -1
    return dp[-1][-1] if dp[-1][-1] != float('inf') else -1


# input 
banyak = int(input("Masukkan jumlah uang: "))
koin = list(map(int, input("Masukkan daftar nilai koin (pisahkan dengan spasi): ").split()))
jumlah = list(map(int, input("Masukkan daftar jumlah koin (sesuai urutan nilai koin, pisahkan dengan spasi): ").split()))

# run fungsi
result = mincoin(banyak, koin, jumlah)

if result == -1:
    print("Tidak dapat mencapai jumlah uang dengan kombinasi koin yang diberikan.")
else:
    print(f"Jumlah minimum koin yang diperlukan: {result}")
