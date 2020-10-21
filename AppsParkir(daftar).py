print("========Apps Parkir========")
print("===========================")
 
id = input("Masukkan ID    : ")
nama = input("Masukkan Nama  : ")
plat = input("Masukkan Plat  : ")

f = open("database.txt","w")
f.write(id+" "+nama+" "+plat)
f.close()