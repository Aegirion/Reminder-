def add(gorev):
    reminder.append(gorev)
    print("Görev eklendi.")

def rmv(gorev):
    if gorev in reminder:
        reminder.remove(gorev)
        print("Görev silindi.")
    else:
        print("Görev bulunamadı.")

def shv():
    print("Aktif görevler:")
    for i, gorev in enumerate(reminder):
        print(f"{i+1}. {gorev}")

print("Hoşgeldiniz!")
print()
reminder = []

while True:
    print("1- Görev ekle\n2- Görev sil\n3- Aktif görevleri listele\n4- Çıkış")
    print()
    secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))

    if secim == 1:
        gorev = input("Eklenecek görevi giriniz: ")
        add(gorev)


    elif secim == 2:

        gorev2 = input("Silinecek görevi giriniz: ")

        if gorev2 in reminder:

            rmv(gorev2)
            print("Görev silindi")

        else:
            print("Görev bulunamadı")


    elif secim == 3:
        shv()

    elif secim == 4:
        print("Program sonlandırılıyor...")
        break

    else:
        print("Geçersiz seçim. Tekrar deneyin.")
