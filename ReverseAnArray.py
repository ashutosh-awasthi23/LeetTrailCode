li = [1,2,3,4,5,6]
fp = 0
bp = len(li)-1
temp = 0
while fp < bp:
    temp = li[fp]
    li[fp] = li[bp]
    li[bp] = temp
    fp = fp + 1
    bp = bp - 1
print(li)
        