
pin = "3328"  
saldo = 500000      
maks_percobaan = 3      
percobaan = 0         

# masukkan PIN
while percobaan < maks_percobaan:
    pin = input("Masukkan PIN: ")
    if pin == pin:
        print("PIN benar! silakan lanjutkan.")
        break
    else:
        percobaan += 1
        print(f"PIN salah! anda memiliki {maks_percobaan - percobaan} percobaan tersisa.")
        
if percobaan == maks_percobaan:
    print("habis batas percobaan PIN. Akun terkunci.")
else:
    # uang yang ingin ditarik
    try:
        jumlah_tarik = float(input("Masukkan jumlah yang ingin ditarik: "))
        # memeriksa saldo
        if jumlah_tarik > saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            saldo -= jumlah_tarik
            print(f"penarikan berhasil! saldo akhir adalah: {saldo:.2f}")
    except ValueError:
        print("masukkan jumlah yang valid.")
