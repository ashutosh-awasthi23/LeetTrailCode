li =  [1,2,4,8,3]
dicto = {li[i]:i for i in range(len(li))}
target = 5
i =0 
while i < len(li):
    complement = target - li[i]
    if complement in dicto and dicto[complement]!=i:
        print(True)
        break
    i +=1
        
        





    
    
    
    
    
    
     
 