import os
import sys

def paketleri_yukle(pip_komut):
    """
    Belirtilen pip komutunu kullanarak gerekli paketleri yükler.
    """
    try:
        paketler = ["requests", "asyncio", "aiohttp", "fade"]
        for paket in paketler:
            os.system(f"{pip_komut} install {paket}")
        print("Paketler başarıyla yüklendi.")
    except Exception as hata:
        print(f"Paket yükleme sırasında bir hata oluştu: {hata}")

def bagimliliklari_yukle():
    """
    İşletim sistemine uygun bağımlılıkları yükler.
    """
    try:
        if sys.platform.startswith("linux"):
            os.system("sudo apt-get update && sudo apt-get install -y python3 python3-pip")
        elif sys.platform.startswith("win"):
            os.system("winget install Python.Python.3")
        else:
            print("Bu işletim sistemi için otomatik bağımlılık yükleme desteklenmiyor.")
    except Exception as hata:
        print(f"Bağımlılık yükleme sırasında bir hata oluştu: {hata}")

def ana():
    """
    Kullanıcıdan pip veya pip3 seçimini alır ve yükleme işlemlerini başlatır.
    """
    secim = input("Ortamınızı seçin: [0] pip / [1] pip3 : ")

    if secim == "0":
        bagimliliklari_yukle()
        paketleri_yukle("pip")
    elif secim == "1":
        bagimliliklari_yukle()
        paketleri_yukle("pip3")
    else:
        print("Geçersiz seçim! Lütfen sadece 0 veya 1 girin.")

if __name__ == "__main__":
    ana()
