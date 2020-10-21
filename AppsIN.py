id = input("Masukkan Id     : ")
masuk = input("Waktu Masuk     : ")
plat = input("Masukkan Plat   : ")

f = open("Transaksi.txt","w")
f.write(id+" "+masuk+" "+plat)
f.close()
