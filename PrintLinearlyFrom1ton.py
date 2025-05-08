def myFunc(n):
    if n <=0:
        return 
    else:
        myFunc(n-1)
        print(n)
    
myFunc(5)