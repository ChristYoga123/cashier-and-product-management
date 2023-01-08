import hashlib as hs
import json

import os
def menu():
    while True:
        os.system("cls")
        print("==" * 20)
        print("Manajemen Produk dan Kasir Toko Ceria")
        print("==" * 20)
        menu = int(input("1. Daftar\n2. Masuk\nPilih menu: "))
        if menu == 1:
            daftar()
        elif menu == 2:
            masuk()

def daftar():
    os.system("cls")
    print("==" * 20)
    print("Daftar Akun")
    print("==" * 20)

    nama = input("Masukkan nama: ")
    password = input("Masukkan password: ")
    confirm_password = input("Masukkan konfirmasi password: ")
    if password != confirm_password:
        input("Password dan Konfirmasi Password kurang tepat. Tekan Enter untuk kembali.")
        daftar()
    akun = {}
    akun["nama"] = nama
    akun["password"] = hs.sha256(password.encode()).hexdigest()

    # Get All Data
    with open("akun.json", "r") as data:
        reader = json.load(data)
    # Entry all input data and rewrite the json file
    reader.append(akun)
    with open("akun.json", "w") as data:
        json.dump(reader, data, indent=4)

def masuk():
    os.system("cls")
    print("==" * 20)
    print("Login Akun")
    print("==" * 20)

    nama = input("Masukkan nama: ")
    password = input("Masukkan password: ")
    password = hs.sha256(password.encode()).hexdigest()
    
    with open("akun.json", "r") as data:
        reader = json.load(data)
    
    akun_auth = {}
    for i in reader:
        if nama == i["nama"]:
            akun_auth["nama"] = i["nama"]
            akun_auth["password"] = i["password"]
    if akun_auth == {}:
        while True:
            jawaban = int(input("Akun belum terdaftar. Ingin mendaftar?\n1. Ya\n2. Tidak\nPilih menu: "))
            if jawaban == 1:
                daftar()
            elif jawaban == 2:
                break
        exit
    else:
        if password != akun_auth["password"]:
            while True:
                jawaban = int(input("Akun belum terdaftar. Ingin mendaftar?\n1. Ya\n2. Tidak\nPilih menu: "))
                if jawaban == 1:
                    daftar()
                elif jawaban == 2:
                    break
            exit
        else:
            input("Login sukses. Tekan Enter untuk lanjut")
            import main as m
            m.dashboard()

menu()