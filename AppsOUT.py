id = input("Masukkan Id   : ")
keluar = input("Waktu Keluar  : ")
plat = input("Masukkan Plat : ")
harga = 0 

f = open("Transaksi.txt","r+")
T= f.read()
LT = T.split()
#print(LT)
def valid(id,plat):
    if id == LT[0] and plat == LT [2]:
        return " VALID BRAYY"    
    else:
        return " INVALID BRAYY"
def total (masuk,keluar):
    harga = (int(keluar) - int(masuk)) * 1000
    return harga

cek = valid(id,plat) 
if cek =="VALID BRAYY":
    harga = total(keluar,LT[1])
else:
    print("404 NOT FOUND !!")
f.close()
print(harga)