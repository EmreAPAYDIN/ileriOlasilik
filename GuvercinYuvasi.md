# GÜVERCİN YUVASI ALGORİTMASI 

## Problem:

Standart 52 karttan oluşan bir iskambil destesinden 5 kart alırsak,en az iki tanesi aynı türden kart olacaktır.Bu durumun güvercin yuvası prensibine göre ıspatının yapılması.

Kart türleri;kupa,karo,maça,sinek

## Çözüm:

5 kartın her biri dört kart türünden birine aittir.Güvercin yuvası prensibine göre,iki yada daha fazla kart aynı kart türüne ait olacaktır.

Kaynak kodlar aşağıdaki gibidir.

Güvercin yasası prensbinin genel formülü gereği yuvalara düşecek ortalama değer bulunur.Ortalama değer güvercin/element sayısının yuvalara  bölünmesi elde edilir.ortalama değer daha sonra yukarı yuvarlanır.Aşağıda bu işlemi yapan fonksiyon yazılmıştır.Bizi problemimiz için en az 5 kart gerekmektedir.Bunun da kontrolü yapılmıştır.

```
[pigeonhole_algorithm.py]

import math
def pigeonhole_sort(k): 
     if k>4:
        pigeon =math.ceil(k/4)
        return pigeon
    else:
       print("bu ispat için en az 5 kart gerekmektedir!!!") 
   
 ```
   
Aşağıdaki kodlarda ise kullanıcıdan parametre olarak kart sayısını alıp fonksiyona işlemesi için gönderilmiştir.Kullanıcın 52 karta uygun değer girmesi zorunlu tutulmuştur.

```
[pigeonhole_algorithm.py]

while 1:
    k = int (input("elinizde kaç kart var? :"))
    if k<0 or k>52 :
        print("0-52 arasında değer giriniz")
    else:
        print("Aynı türden kağıt sayısı:", end = ' ') 
        b=pigeonhole_sort(k)     
        print(b)
 ```      
Örnek ekran çıktısı:

 elinizde kaç kart var? :5
 Aynı türden kağıt sayısı: 2

 elinizde kaç kart var? :10
 Aynı türden kağıt sayısı: 3
 
 elinizde kaç kart var? :89
 0-52 arasında değer giriniz

 elinizde kaç kart var? :-5
 0-52 arasında değer giriniz

Kaynak kod için:pigeonhole_algorithm.py
