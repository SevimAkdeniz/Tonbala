import random

def kartOlustur():
    kartsayilari = random.sample(range(1,91),15)

    random.shuffle(kartsayilari)

    dizi1=  []

    for i in range(0, 15, 5):
        dizi1.append(kartsayilari[i:i+5])

    return dizi1


kartlaracikmi = True
kartlar = []
oyuncular = []
sayac =0
sayilar= list(range(1, 91))
random.shuffle(sayilar)
puanlar = { 

}

while (True):
    OyuncuSayisi = int(input("Lutfen oyuncu sayisini giriniz (2-5) : "))  
    if (OyuncuSayisi>=2 and OyuncuSayisi<=5 ):
        break

for i in range(OyuncuSayisi):
    oyuncular.append(input(str(i+1)+". Oyuncunun ismini giriniz : "))
    puanlar[oyuncular[i]] = 0

for i in range(OyuncuSayisi):
    kartlar.append(kartOlustur())
    
for i in kartlar:
    print(str(oyuncular[sayac])+" Adli Oyuncunun karti : ")
    sayac= sayac+1
    for j in i:
     
     print(j)

sayac = 0
while(kartlaracikmi):
    cekilenSayi = sayilar[sayac]
    print(cekilenSayi)
    sayac1 = 0
    for i in kartlar:
        print(str(oyuncular[sayac1])+" Adli Oyuncunun karti : ")
        sayac1= sayac1+1
        for j in i:
            print(j)
    
    for i in range(len(kartlar)):  
        for j in range(len(kartlar[i])): 
            for k in range(len(kartlar[i][j])): 
                if kartlar[i][j][k] == cekilenSayi:
                    kartlar[i][j][k] = 0 
                
    for i in range(len(kartlar)):
        if kartlar[i] == [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]:
            print("tombala")
            puanlar[oyuncular[i]] +=15
            kartlaracikmi = False
        for j in range(len(kartlar[i])):
            if kartlar[i][j] == [0,0,0,0,0]:
                kartlar[i][j] = [-1,-1,-1,-1,-1]
                puanlar[oyuncular[i]] +=5
    
    sayac = sayac+1
    

for isim, puan in puanlar.items():
   print(f"{isim}: {puan}")









    






    
    


     




   

    

       
        
   

        

   








