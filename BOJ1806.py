import sys
a,b =list(map(int,sys.stdin.readline().rstrip().split()))
lst =list(map(int,sys.stdin.readline().rstrip().split()))
if (sum(lst)<b):
    print(0)
    exit()
minn = 10000000134
for i in range(len(lst)):
    tmp = 0
    cnt = 0
    for j in range(i,len(lst)):
        tmp+=lst[j]
        if tmp>=b:
            if minn>j-i+1:
                minn = j-i+1
                break
print(minn)