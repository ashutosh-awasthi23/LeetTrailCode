def Reverse(arr,si,ei):
    if si< ei:
        arr[si],arr[ei] = arr[ei],arr[si]
        Reverse(arr,si+1,ei-1)

arr = [1,2,3,4,5,6]
print(arr)
Reverse(arr,0,len(arr)-1)
print(arr)