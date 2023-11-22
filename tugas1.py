import os


def ascending(bil):
    for i in range(len(bil)):
        for j in range(len(bil) - i - 1):
            if bil[j] > bil[j + 1]:
                bil[j], bil[j + 1] = bil[j + 1], bil[j]
    print("Data setelah diurutkan : ", bil)


def descending(bil):
    for i in range(len(bil)):
        for j in range(len(bil) - i - 1):
            if bil[j] < bil[j + 1]:
                bil[j], bil[j + 1] = bil[j + 1], bil[j]
    print("Data setelah diurutkan : ", bil)


bil = []
while True:
    os.system("cls")
    print("program mengurutkan data")
    print("Dengan metode Bubble Sort")
    jumlahAngka = int(input("Masukan jumlah angka yang mau diurutkan : "))
    for i in range(jumlahAngka):
        angka = int(input(f"Masukan jumlah angka {i + 1}: "))
        bil.append(angka)
    print("========================")
    print("Pilih Metode pengurutan \n 1.Sorting ascending \n 2.Sorting descending")
    sorting = int(input("Masukan pilihan : "))
    print("Data sebelum diurutkan : ", bil)
    print("nilai maks = " + str(max(bil)))
    print("nilai min = " + str(min(bil)))
    print("rata-rata = " + str(sum(bil) / len(bil)))
    if sorting == 1:
        ascending(bil)
    elif sorting == 2:
        descending(bil)

    loop = input("Apakah ingin melanjutkan ? (y/n) ")
    if (loop != "y") and (loop != "Y"):
        print("masukan y untuk melanjutkan")
        break
    elif loop == "n" or loop == "N":
        print("terimakasih")
        break