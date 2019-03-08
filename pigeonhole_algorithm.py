
import math
# Python program to implement Pigeonhole Sort */ 
  
# source code : "https://en.wikibooks.org/wiki/ 
#   Algorithm_Implementation/Sorting/Pigeonhole_sort" 
def pigeonhole_sort(k): 
    # size of range of values in the list  
    # (ie, number of pigeonholes we need) 
    if k>4:
        pigeon =math.ceil(k/4)
        return pigeon
    else:
       print("bu ispat için en az 5 kart gerekmektedir!!!") 
    
     
    
  
    
  
    


# In[14]:

while 1:
    k = int (input("elinizde kaç kart var? :"))
    print("Aynı türden kağıt sayısı:", end = ' ') 
    b=pigeonhole_sort(k)     
    print(b)
