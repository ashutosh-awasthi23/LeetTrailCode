def myFunc(N):
    if N<=0:
        return
    else:
        print(N)
        myFunc(N-1)
myFunc(10)