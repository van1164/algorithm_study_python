a = int(input())
lst = {}
for i in range(a):
    x = int(input())
    if x in lst:
        lst[x]+=1
    else:
        lst[x]=1
maxx =0
tmp =0
for i in lst:
    if lst[i]>maxx:
        maxx = lst[i]
        tmp = i
    elif lst[i]==maxx and i<tmp:
        tmp = i
print(tmp)