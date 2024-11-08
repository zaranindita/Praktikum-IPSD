# soal no 2
def urutganjil(list1, list2):
    # ambil elemen dari masing2 list
    listangka= list1[1::2] + list2[1::2]
    # mengurutkan angka
    listangka.sort(reverse=True)
    return listangka

# meminta input 
def inputlist(prompt):
    return list(map(int, input(prompt).split()))

# main program
def main():
    print("Masukkan angka untuk list ke-1, dipisahkan dengan spasi:")
    list1 = inputlist("List 1: ")
    
    print("Masukkan angka untuk list ke-2, dipisahkan dengan spasi:")
    list2 = inputlist("List 2: ")
    
    hasil = urutganjil(list1, list2)
    print("urutan elemen dengan indeks ganjil secara menurun:")
    print(hasil)

if __name__ == "__main__":
    main()
