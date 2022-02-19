import sys
a= int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
sett =sorted(list(set(lst)))
dic=dict()
for i in range(len(sett)):
    dic[sett[i]] = i

for i in lst:
    print(dic[i],end=' ')