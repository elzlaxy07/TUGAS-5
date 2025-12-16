barang1 = "Kitkat"
harga1 = 15000
barang2 = "Glico Pocky"
harga2 = 9000
barang3 = "Bourbon Alfort Mini Chocolate"
harga3 = 30500
barang4 = "Lotte Koala's March"
harga4 = 12000
barang5 = "Glico Pretz"
harga5 = 9000

print("SELAMAT DATANG DI TOKO UCHIHA")
print("List Item:")
print("- " + barang1 + ": Rp " + str(harga1))
print("- " + barang2 + ": Rp " + str(harga2))
print("- " + barang3 + ": Rp " + str(harga3))
print("- " + barang4 + ": Rp " + str(harga4))
print("- " + barang5 + ": Rp " + str(harga5))

total = 0

print("\nSilakan belanja:")
print("Ketik 'Tidak ada' jika sudah tidak ada item lain yang akan dibeli.")
while True:
    beli = input("Mau beli apa? ")

    nama_barang = ""
    jumlah_barang = 0
    harga_barang = 0

    if beli == "Tidak ada":
        break
    elif beli == barang1:
        jumlah_barang = int(input("Jumlah: "))
        harga_barang = harga1
        nama_barang = barang1
    elif beli == barang2:
        jumlah_barang = int(input("Jumlah: "))
        harga_barang = harga2
        nama_barang = barang2
    elif beli == barang3:
        jumlah_barang = int(input("Jumlah: "))
        harga_barang = harga3
        nama_barang = barang3
    elif beli == barang4:
        jumlah_barang = int(input("Jumlah: "))
        harga_barang = harga4
        nama_barang = barang4
    elif beli == barang5:
        jumlah_barang = int(input("Jumlah: "))
        harga_barang = harga5
        nama_barang = barang5
    else:
        print("Barang tidak ada")
        continue

    subtotal = jumlah_barang * harga_barang
    total = total + subtotal

    print("Anda beli " + str(jumlah_barang) + " x " + nama_barang + " = Rp " + str(subtotal))

print("\nStruk Pembelian:")
print("Total: Rp " + str(total))

uang = int(input("\nUang yang dibayar: Rp "))
kembalian = uang - total
print("Kembalian: Rp " + str(kembalian))
print("Arigatou Gozaimasu!")