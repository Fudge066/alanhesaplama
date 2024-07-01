print("""
1- Dikdörtgenin alanı
2- Dikdörtgenin çevresi
3- Karenin Alanı
4- Karenin çevresi
5- Yamuğun Alanı
6- Paralelkenar Alanı
9- Çıkış
""")

while True:
    secim = input("Yapılacak işlemi seçin (çıkış için '9'ı basın): ")

    if secim == '9':
        print("Çıkış yapılıyor...")
        break
    
    elif secim == '1':
        kkenar = float(input("Kısa kenarı giriniz: "))
        ukenar = float(input("Uzun kenarı giriniz: "))
        print("Dikdörtgenin alanı:", kkenar * ukenar)
    
    elif secim == '2':
        kkenar = float(input("Kısa kenarı giriniz: "))
        ukenar = float(input("Uzun kenarı giriniz: "))
        print("Dikdörtgenin çevresi:", 2 * (kkenar + ukenar))
    
    elif secim == '3':
        kare_kenari = float(input("Karenin bir kenarını giriniz: "))
        print("Karenin alanı:", kare_kenari ** 2)
    
    elif secim == '4':
        kare_kenari = float(input("Karenin bir kenarını giriniz: "))
        print("Karenin çevresi:", kare_kenari * 4)
    
    elif secim == '5':
        y_alt = float(input("Alt taban uzunluğu: "))
        y_ust = float(input("Üst taban uzunluğu: "))
        yukseklik = float(input("Yükseklik: "))
        alan = (y_alt + y_ust) * yukseklik / 2
        print("Yamuğun Alanı:", alan)
    
    elif secim == '6':
        taban_uzunlugu = float(input("Paralelkenarın taban uzunluğunu giriniz: "))
        yukseklik = float(input("Paralelkenarın yüksekliğini giriniz: "))
        print("Paralelkenarın alanı:", taban_uzunlugu * yukseklik)
    
    else:
        print("Geçersiz işlem seçtiniz")
