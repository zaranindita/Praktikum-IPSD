def katadibalik(kalimat):
    # memisahkan string 
    kata2 = kalimat.split()
    # membalikan setiap kata 
    katayangdibalik = [kata[::-1] for kata in kata2]
    return katayangdibalik

# input 
kalimat = input("Masukkan sebuah kalimat: ")
result = katadibalik(kalimat)
print(result)
