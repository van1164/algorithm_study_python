t = int(input())
for i in range(t):
    a,b,c,d = list(map(int,input().split()))
    cnt =0
    boo =False
    while c<=a*b:
        if (c - d) % b == 0:
            cnt+=c
            boo=True
            break
        c += a
            
    if boo:
        print(cnt)
    else:
        print(-1)