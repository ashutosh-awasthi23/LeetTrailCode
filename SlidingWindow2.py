li = [1,2,2,-1,-1,1,-2]
length = len(li)
sumy = 0
dicto = {i:0 for i in range(length)}
for i in range(1 ,length):
    sumy = sumy + li[i-1]
    dicto[i] = sumy
    
print(dicto)
    
    
    
    
    
     
 