from collections import deque
N = int(input())
lst = list(map(int,input().split()))
plus = deque([])
minus = []
minn = 1000000000000000
for i in range(N):
    if lst[i]<0:
        minus.append(lst[i])
    else:
        plus.appendleft(lst[i])
        
min_length = len(minus)
plus_length= len(plus)
if min_length>=2 and plus_length>=2:
    if abs(plus[-1]+plus[-2])<abs(minus[-1]+minus[-2]):
        minn = abs(plus[-1]+plus[-2])
        tup = (plus[-1],plus[-2])
    else:
        minn = abs(minus[-1]+minus[-2])
        tup = (minus[-2],minus[-1])
elif min_length==0:
    print(plus[-1],plus[-2])
    exit()
elif plus_length ==0:
    print(minus[-2],minus[-1])
    exit()
elif min_length>=2 and plus_length<2:
        minn = abs(minus[-1]+minus[-2])
        tup = (minus[-2],minus[-1])
elif plus_length>=2 and min_length<2:
        minn = abs(plus[-1]+plus[-2])
        tup = (plus[-1],plus[-2])    
else:
    minn = 100000000000000
    tup= (100000,100000)
for i in range(min_length):
    temp_minn = 100000000000000
    min_tup = (1000000,100000)
    for j in range(plus_length):
        if abs(plus[j]+minus[i])<temp_minn:
            temp_minn = abs(plus[j]+minus[i])
            min_tup  = (minus[i],plus[j])
        else:
            if minn>temp_minn:
                minn = temp_minn
                tup = min_tup
            break
    if minn>temp_minn:
        minn = temp_minn
        tup = min_tup
print(min(tup),max(tup))