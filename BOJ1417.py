import sys

N = int(sys.stdin.readline())
lst =[-1]
for i in range(N):
    lst.append(int(sys.stdin.readline()))
idx = lst.index(max(lst))
if idx ==1 and lst.count(lst[1])==1:
    print(0)
else:
    fin = lst[1]
    lst = lst[2:]
    cnt = 0
    idx-=2
    while True:
        cnt+=1
        fin+=1
        lst[idx]-=1
        idx = lst.index(max(lst))
        if lst[idx]<fin:
            break
    print(cnt)