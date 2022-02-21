a = int(input())
lst = []
for i in range(a):
    lst.append(tuple(map(int,input().split())))
lst  =sorted(lst,key=lambda x:(x[1],x[0]))
start = 0
cnt = 0
for i in range(len(lst)):
    if lst[i][0]<start:
        continue
    else:
        cnt+=1
        start = lst[i][1]
print(cnt)