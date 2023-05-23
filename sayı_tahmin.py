import random
import time

print("************** Sayı Tahmin oyunu \n 1 ile 40 arasında sayıyı tahmin edin. \n************** ")

rasgele_sayı =random.randint (1,40)
tahmin_hakkı = 7
while True:
    tahmin= int(input("Tahmininiz:"))

    if(tahmin<rasgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin.....")

        tahmin_hakkı -= 1

    elif (tahmin > rasgele_sayı):
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin....")

        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler! Sayımız",rasgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız bitti....")
        print("Sayımız:",rasgele_sayı)
        break