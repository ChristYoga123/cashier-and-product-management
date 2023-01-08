def dashboard():
    menu = int(input("1. Menu Produk\n2. Kasir\n3. Logout\nPilih menu: "))
    if menu == 1:
        print("Menu Produk")
    elif menu == 2:
        print("Kasir")
    elif menu == 3:
        exit