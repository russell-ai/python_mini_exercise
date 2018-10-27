# Bilgisayarın 1 ila 100 arası kullanınücının tuttuğu rakamı tahmin etmeye yarayan program
cevap = 'yes'
print ("Lütfen 1'den 100'a kadar olan rakamlardan bir sayı aklınızdan tutun. Ben de en fazla 10 hakkımda bulmaya çalışacağım. ")
while cevap == "yes":
    Deneme_hakkı = 10
    tahmin = 50
    altlimit = 1
    üstlimit = 100
    while Deneme_hakkı != 0:
        try:
            print("Tahminim: ", tahmin)
            print("Tahminim Yüksekse : 1 ")
            print("Tahminim Düşükse  : 2 ")
            print("Tahminim Doğru ise: 3  Rakamını girininiz!")
            kullanıcıcevabı = int(input("Tahminim Nasıl?"))
            if 1 < kullanıcıcevabı > 3:
                print("Lütfen doğru bir rakam girin. 1, 2 ve 3 geçerli numaralardır.")
                Deneme_hakkı = Deneme_hakkı + 1
            if kullanıcıcevabı == 1:
                üstlimit = tahmin
                print("Hmm, sanırım tuttuğun rakam aralığı ", altlimit, "ve ", üstlimit, "dir.")
                Deneme_hakkı = Deneme_hakkı - 1
                print(Deneme_hakkı, " Hak Kaldı.")
                tahmin = int (((üstlimit - altlimit) / 2) + altlimit)
                if tahmin <= altlimit:
                    tahmin = tahmin + 1
                if üstlimit - altlimit == 2:
                    tahmin = altlimit + 1
            elif kullanıcıcevabı == 2:
                altlimit = tahmin
                print("Hmm, sanırım tuttuğun rakam aralığı ", altlimit, "ve ", üstlimit, "dir.")
                Deneme_hakkı = Deneme_hakkı - 1
                print(Deneme_hakkı, " Hak Kaldı.")
                tahmin = int (((üstlimit - altlimit) / 2) + altlimit)
                if tahmin <= altlimit:
                    tahmin = tahmin + 1
                if üstlimit - altlimit == 2:
                    tahmin = altlimit + 1
            elif kullanıcıcevabı == 3:
                print("Oley! Ben Kazandım!")
                Deneme_hakkı = 0
        except:
            break
    else:
        cevap = input(' Oyuna devam etmek istermisiniz? (yes/no)')

else:
    print("Oyun için teşekkürler. Güle Güle!")