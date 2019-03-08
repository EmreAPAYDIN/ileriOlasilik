#GÜVERCİN YUVASI PRENSİBİ
#Standart 52 karttan oluşan bir iskambil destesinden 5 kart alırsak,
#en az iki tanesi aynı türden kart olacaktır.kart türleri;kupa,karo,maça,sinek

    #5 kartın her biri dört kart türünden birine aittir. 
    #güvercin yuvası prensibine göre,iki yada daha fazla kart aynı kart türüne 
    #ait olacaktır.
import math

def pigeonhole_sort(k): 
   
    if k>4:
        pigeon =math.ceil(k/4) #güvercin yasası prensbinin genel formülü gereği
        #yuvalara düşecek ortalama değer bulunur.Ve yukarı yuvarlanır.
        return pigeon
    else:
       print("bu ispat için en az 5 kart gerekmektedir!!!") 
    
     
while 1:
    k = int (input("elinizde kaç kart var? :"))
    if k<0 or k>52 :
        print("0-52 arasında değer giriniz")
    else:
        print("Aynı türden kağıt sayısı:", end = ' ') 
        b=pigeonhole_sort(k)     
        print(b)
    
     
    
  
    
  
    

