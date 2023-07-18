def checkBit(a,b):
    return 1 if a&(1<<b)!=0 else 0
print(checkBit(*map(int,input().split())))