import os,csv
import prettytable
import pandas as pd
import sys
import time

os.system("cls")


def tampilanAwal() :
    print("=" *45)
    print("=                                           =")  
    print("=            selamat datang di ADIG         =")
    print("=                                           =")
    print("=" *45)


def menu():
    os.system('cls')
    print('\033[92m==============================\033[0m')
    print(f"\033[92mHai.. \033[0m{user}")
    print('\033[92m==============================\033[0m')
    print("""Pilih provinsi""")
    print("1. Jawa Timur")
    print("2. Jawa Tengah")
    print("3. Jawa Barat")
    print('4. EXITT')
    pil=input("\nmasukkan nomor provinsi : ")
    if pil == '1':
        jawaTimur()
    elif pil == '2':
        jawaTengah()
    elif pil == '3':
        jawaBarat()
    elif pil == '4':
        os.system('cls')
    else :
        menu()
    
def jawaTimur():
    os.system('cls')
    print('JAWA TIMUR')
    print('==========')
    print("1. Bangkalan\n2. Blitar\n3. Bojonegoro\n4. Gresik\n5. Jember\n6. Jombang\n7. Kediri\n8. Lamongan\n9. Madiun\n10. Banyuwangi\n\n11. Kembali")
    aa = input("Masukan Nomor Kota :")
    if aa == '1':
        os.system('cls')
        ####Siniiiiii ngasih nama kabupaten
        dataku = 'bangkalan.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '2' :
        os.system('cls')
        dataku = 'blitar.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '3' :
        os.system('cls')
        dataku = 'bojonegoro.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '4' :
        os.system('cls')
        dataku = 'gresik.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '5' :
        os.system('cls')
        dataku = 'jember.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '6' :
        os.system('cls')
        dataku = 'jombang.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '7' :
        os.system('cls')
        dataku = 'kediri.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '8' :
        os.system('cls')
        dataku = 'lamongan.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '9' :
        os.system('cls')
        dataku = 'madiun.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '10' :
        os.system('cls')
        dataku = 'banyuwangi.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTimur()
    elif aa == '11':
        menu()
    else :
        jawaTimur()
    
def jawaTengah():
    os.system('cls')
    print('JAWA TENGAH')
    print('==========')
    print("1. Bajarnegara\n2. Banyumas\n3. Blora \n4. Boyolali\n5. Cilacap\n6. Karanganyar\n7. Kebumen\n8. Klaten\n9. Kudus\n10. Magelang\n\n11. Kembali")
    aa = input("Masukan Nomor Kota :")
    if aa == '1':
        os.system('cls')
        dataku = 'banjarnegara.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '2' :
        os.system('cls')
        dataku = 'banyumas.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '3' :
        os.system('cls')
        dataku = 'blora.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '4' :
        os.system('cls')
        dataku = 'boyolali.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '5' :
        os.system('cls')
        dataku = 'cilacap.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '6' :
        os.system('cls')
        dataku = 'karanganyar.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '7' :
        os.system('cls')
        dataku = 'kebumen.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '8' :
        os.system('cls')
        dataku = 'klaten.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '9' :
        os.system('cls')
        dataku = 'kudus.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '10' :
        os.system('cls')
        dataku = 'magelang.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaTengah()
    elif aa == '11':
        menu()
    else :
        jawaTengah()
def jawaBarat():
    os.system('cls')
    print('JAWA BARAT')
    print('==========')
    print("1. Cianjur\n2. Cirebon\n3. Garut\n4. Karawang\n5. Subang\n6. Sumedang\n7. Tasikmalaya\n8. Bandung\n9. Cimahi\n10. Sukabumi\n\n11. Kembali")
    aa = input("Masukan Nomor Kota :")
    if aa == '1':
        os.system('cls')
        dataku = 'cianjur.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '2' :
        os.system('cls')
        dataku = 'cirebon.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '3' :
        os.system('cls')
        dataku = 'garut.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '4' :
        os.system('cls')
        dataku = 'karawang.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '5' :
        os.system('cls')
        dataku = 'subang.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '6' :
        os.system('cls')
        dataku = 'sumedang.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '7' :
        os.system('cls')
        dataku = 'tasikmalaya.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '8' :
        os.system('cls')
        dataku = 'bandung.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '9' :
        os.system('cls')
        dataku = 'sukabumi.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '10' :
        os.system('cls')
        dataku = 'cimahi.csv'
        with open(dataku) as buka_file:
            print(prettytable.from_csv(buka_file))
        input('Klik [ENTER] Untuk Kembali')
        jawaBarat()
    elif aa == '11':
        menu()
    else :
        jawaBarat()
tampilanAwal()

while True:
    print("====================================")
    Pilihan = input("Apakah Anda Memiliki Akun?[yes/no] : ")
    if Pilihan == "yes":
        os.system('cls')
        while True :
            print('''=========>Silakan Login<=======\n''')
            file = "login.txt"
            opn = open(file)
            List =  opn.readlines()
            user = input('Username :')
            pasw = input('Password :')
            os.system('cls')
            Data = []
            sukses = False
            for i in List:
                Data.append(i.strip())
            for i in range(0,len(List),2):
                if user == Data[i]:
                    if pasw == Data[i+1]:
                        sukses = True
                        break
                    else :
                        print('--------------------------------------')
                        print('Password Salah Tekan [ENTER] Coba Lagi')
                        print('--------------------------------------')
                        input()
                        os.system("cls")
                        continue
            if sukses:
                menu()
                break
            else:
                print('--------------------------------------')
                print('Password Salah Tekan [ENTER] Coba Lagi')
                print('--------------------------------------')
                input()
                os.system("cls")
                continue
        break
    elif Pilihan == "no":
        os.system('cls')
        print("""=====>>Buat Akun Baru<<=====""")
        file = "login.txt"
        name = input("Masukan Username Baru : ")
        pasw = input("Masukan Password Baru : ")
        while True:
            psw2 = input("Masukan Ulang Password :")
            if pasw==psw2:
                opn = open(file,"a")
                opn.write(f"{name}\n{pasw}\n")
                opn.close()
                break
            else:
                print(f'=====>>Password Tidak Sama<<=====')
                continue
        input("=========>>Data Tersimpan Silahkan Login<<=========")
        os.system('cls')
        continue
    

