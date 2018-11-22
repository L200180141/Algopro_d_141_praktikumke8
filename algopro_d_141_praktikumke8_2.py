########nama = aji mustaqim
########nim = l200180141
########
########
##########o={'NIM' : 'L200180141', 'Nama' : 'Aji Mustaqim', 'Alamat' : 'Karanganyar',
##'Hobby' : 'Futsal','JenisKelamin' : 'Laki-Laki','Agama' : 'Islam','Umur' : '18'}
##
##def NIM():
##    print "NIM : ", o['NIM']
##def Nama():
##    print "Nama : ",o['Nama']
##def Alamat():
##    print "Alamat : ",o['Alamat']
##def Hobby():
##    print "Hobby : ",o['Hobby']
##def JenisKelamin():
##    print "jenisKelamin : ",o['JenisKelamin']
##def Agama():
##    print "Agama : ",o['Agama']
##def Umur():
##    print "Umur : ",o['Umur']
##pilihan = "kosong"
##while pilihan != "k":
##    pilihan = raw_input("Masukkan pilihan anda: ")
##    if pilihan == "a":
##            NIM()
##    elif pilihan == "b":
##            Nama()
##    elif pilihan == "c":
##            Alamat()
##    elif pilihan == "d":
##            Hobby()
##    elif pilihan == "e":
##            JenisKelamin()
##    elif pilihan == "f":
##            Agama()
##    elif pilihan == "g":
##            Umur()
##    elif pilihan == "p":
##            print '''
##Daftar Pilihan yang tersedia:
##a menampilkan NIM
##b menampilkan Nama
##c menampilkan Alamat
##d menampilkan Hobby
##e menampilkan Jeniskelamin
##f menampilkan Agama
##g menampilkan Umur
##k menampilkan Keluar
##p menampilkan Bantuan
##'''
##    elif pilihan == "k":
##            print "Terima Kasih."
##    else:
##            print "perintah tidak dikenal"

##kegiatan 2

def konversisuhu(c = 0, f = 0):
    "fungsi mengkonversi suhu celcius ke fahrenheit dan sebaliknya"
    if c != 0:
        y = ((9*c/5)+32)
        print "suhu", c, "celcius setara dengan", y, "fahrenheit"
    elif f != 0:
        b = ((f-32)*5/9)
        print "suhu", f, "fahrenheit setara dengan", b, "celcius"
    else :
        print("suhu 0 celcius setara dengan 32 fahrenheit")
    return;

        



