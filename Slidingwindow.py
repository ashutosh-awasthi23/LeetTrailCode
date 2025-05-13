li = [1,2,2,1,1,1,2]
length = len(li)
i = 0 
j = 0
maxi = 0
sumy = li[0]
target = 5
count = 0
while j<length:
    if sumy > target:
        sumy  =sumy -li[i]
        i+=1
    elif sumy  < target:
        j=j+1
        if j < length:
            sumy += li[j]
        
    else:
        count = count + 1
        sumy = sumy - li[i]
        i=i+1
        j=j+1
        if j < length:
            sumy += li[j]
        
print(count)
    
        
        