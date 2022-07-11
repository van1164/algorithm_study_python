S = input()
lst = []
x=-1
length = len(S)
while True:
    x+=1
    if x>=length:
        break
    if S[x] =='X':
        cnt=1
        while True:
            x+=1
            if x>=length:
                break
            if S[x]=='X':
                cnt+=1
            else:
                break
        lst.append('AAAA'*(cnt//4))
        cnt-=(cnt//4)*4
        lst.append('BB'*(cnt//2))
        cnt-=(cnt//2)*2
        if cnt!=0:
            print(-1)
            exit()
    else:
        lst.append('.')
for a in lst:
    print(a,end='')