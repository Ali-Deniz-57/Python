
print("""*********
Hesap Makinesi 
Toplama = 1
Çıkarma = 2
Çarpma = 3
Bölme = 4
Üs almak için = 5
Sayının karekökünü almak için = 6 
Sayının logaritması için = 7
dereceyi radyana çevirmek için = 8
radyanı dereceye çevirmek için = 9
sinüs ü bulmak için = 10
cos u bulmak için = 11
tanjantı bulmak için = 12
cotanjantı bulmak için = 13
Çıkmak için q ya basın...

#sin cos tan cot bunlarda radyan cisnsinden buluyor.
*********""")
import time 
import math

while True:
    işlem = int(input("İşleminizi Giriniz: "))

    if(işlem=="q"):
        print("İşlem sonlandırılıyor...")
        time.sleep(1)
        print("Tekrar Bekleriz")
        break

    elif(işlem==1):
        sayı1=int(input("1. Sayıyı Giriniz:"))
        sayı2=int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} + {} = {}".format(sayı1,sayı2,sayı1+sayı2))

    elif(işlem==2):
        sayı1=int(input("1. Sayıyı Giriniz:"))
        sayı2=int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayı1,sayı2,sayı1-sayı2))

    elif(işlem==3):
        sayı1=int(input("1. Sayıyı Giriniz:"))
        sayı2=int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} * {} = {}".format(sayı1,sayı2,sayı1*sayı2))

    elif(işlem==4):
        sayı1=int(input("1. Sayıyı Giriniz:"))
        sayı2=int(input("2. Sayıyı Giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} / {} = {}".format(sayı1,sayı2,sayı1/sayı2))

    elif(işlem==5):
        sayı1=int(input("Üsü alınacak sayıyı giriniz:"))
        sayı2=int(input("üssü giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} ^ {} = {}".format(sayı1,sayı2,math.pow(sayı1,sayı2)))

    elif(işlem==6):
        sayı1=int(input("Karakökü alınacak sayıyı giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1) 
        print("{} sayısının karakökü = {}".format(sayı1,math.sqrt(sayı1)))

    elif(işlem==7):
        sayı1=int(input("1. Sayıyı Giriniz:"))
        sayı2=int(input("Taganını giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} sayısının  {} tabanının logaritması = {}".format(sayı1,sayı2,math.log(sayı1,sayı2)))

    elif(işlem==8):
        sayı1=int(input("Dereceyi giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} derece  = {} radyanı".format(sayı1,math.degrees(sayı1)))

    elif(işlem==9):
        sayı1=int(input("Radyanı giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("{} radyan = {} derecedir".format(sayı1,math.radians(sayı1)))

    elif(işlem==10):
        a= input("radyan için =R , derece için = D")
        if(a =="r" or a== "R"):
            sayı1=int(input("sayıyı giriniz:"))
            x = math.sin(sayı1)
            print("İşleminiz Yapılıyor...")
            time.sleep(1)
            print("sin {} = {}".format(sayı1,x))
        
        elif(a == "d" or a == "D"):
            sayı1 = int(input("Dereceyi giriniz:"))
            x = math.sin(sayı1)
            y = math.radians(x)
            print("İşleminiz Yapılıyor...")
            time.sleep(1)
            print("sin {} = {}".format(sayı1,y))

    elif(işlem==11):
        sayı1=int(input("Derece giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("cos {}  {}".format(sayı1,math.cos(sayı1)))

    elif(işlem==12):
        sayı1=int(input("Derece giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        print("tanjant {}  {}".format(sayı1,math.tan(sayı1)))

    elif(işlem==13):
        sayı1=int(input("Derece giriniz:"))
        print("İşleminiz Yapılıyor...")
        time.sleep(1)
        x= math.cos(sayı1)/math.sin(sayı1)
        print("cotanjant {}  {}".format(sayı1,x))
    
