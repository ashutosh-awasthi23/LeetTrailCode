nums = [2,2,1,1,1,2,2]
count =0
element = None
i = 0
length = len(nums)
while i < length :
    if count ==0:
        element = nums[i]
        count+=1
    elif nums[i]==element:
        count+=1
    else:
        count-=1
    i+=1
print(element)