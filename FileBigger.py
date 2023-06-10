import os

def dosyayi_buyut(dosya_adi, buyutme_miktari, birim):
    try:
        # Dosya boyutunu hesapla
        dosya_boyutu = os.path.getsize(dosya_adi)
        
        # Büyütme miktarını MB cinsinden hesapla
        if birim.lower() == 'gb':
            buyutme_miktari *= 1024  # GB'i MB'ye dönüştür
        elif birim.lower() != 'mb':
            print("Hatalı birim girdisi. Lütfen MB veya GB olarak belirtin.")
            return
        
        # Dosyayı büyüt
        with open(dosya_adi, 'ab') as dosya:
            bos_veri = b'\x00' * int(buyutme_miktari * 1024 * 1024)  # MB'yi byte'a çevir
            dosya.write(bos_veri)
        
        # Dosya boyutunu kontrol et
        yeni_boyut = os.path.getsize(dosya_adi)
        print(f"Dosya başarıyla büyütüldü. Yeni boyut: {yeni_boyut} byte.")
    
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    
    except:
        print("Bir hata oluştu.")

# Kullanıcıdan girişleri al
dosya_adi = input("Dosya adını girin: ")
buyutme_miktari = float(input("Büyütme miktarını girin: "))
birim = input("Birim (MB veya GB) girin: ")

# Dosyayı büyüt
dosyayi_buyut(dosya_adi, buyutme_miktari, birim)
