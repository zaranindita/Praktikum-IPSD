import pandas as pd
import csv

#  membaca file CSV dan simpan di dict
def csvdict (namafile):
    data = {}
    with open (namafile, mode='r') as file:
        bacacsv = csv.reader(file)
        next(bacacsv)  # membaca header
        for baris in bacacsv:
            nama = baris[0]  
            nilai = list(map(float, baris[1:]))  # jadikan float
            data[nama] = nilai  
    return data

#  menghitung rata2 semua mhs
def hitungrata2(data):
    rata2 = {}
    for nama, nilai in data.items():
        if nilai:  # cek daftar nilai 
           rata2[nama] = sum(nilai) / len(nilai)  
    return rata2

# menemukan nilai rata2 tertinggi dan terendah
def caritertinggiterendah(rata2):
    tertinggi = max(rata2, key=rata2.get)
    terendah = min(rata2, key=rata2.get)
    return tertinggi, terendah

# main
def main():
    namafile = 'C:/Users/Admin/Documents/IPSD ASSIGNMENT/modul 1/nilaisiswa.csv'  # Ubah sesuai dengan jalur file di sistem Anda
    data = csvdict (namafile)
    
    rata2 = hitungrata2(data)
    print("Rata-rata nilai tiap mahasiswa:")
    for nama, avg in rata2.items():
        print(f"{nama}: {avg:.2f}")
    
    tertinggi, terendah = caritertinggiterendah (rata2)
    print(f"\nMahasiswa dengan nilai rata-rata tertinggi: {tertinggi} ({rata2[tertinggi]:.2f})")
    print(f"Mahasiswa dengan nilai rata-rata terendah: {terendah} ({rata2[terendah]:.2f})")

if __name__ == "__main__":
    main()
