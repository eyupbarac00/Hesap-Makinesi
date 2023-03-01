import time
import webbrowser

print("Hesap Makinesine Hoş Geldiniz")
print(" | Toplama = 1 \n | Çıkarma = 2 \n | Çarpma = 3 \n | Bölme = 4")
islem = int(input())
if not 0 < islem < 5:
  print("Geçerli bir sayı girin!")
  time.sleep(2)
  exit

elif 0 < islem < 5:
 ilkSayı = int(input("ilk sayıyı giriniz = "))
 ikinciSayı = int(input("ikinci sayıyı giriniz = "))

 if islem == 1:
  print(ilkSayı + ikinciSayı)
 elif islem == 2:
  print(ilkSayı - ikinciSayı)
 elif islem == 3:
  print(ilkSayı * ikinciSayı)
 elif islem == 4:
  print(ilkSayı / ikinciSayı)

time.sleep(2)
print("Eyüp Baraç tarafından yapıldı! 5 saniye içinde github profiline yönlendirileceksiniz!")
time.sleep(5)
webbrowser.open("https://github.com/eyupbarac00") 
