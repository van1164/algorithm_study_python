from itertools import permutations


N,M = list(map(int,input().split()))
lst = list(input().split())
lst.sort()
pre = (-1,-1)
for i in permutations(lst,M):
    if pre == i:
        continue
    else:
        for x in i:
            print(x,end=' ')
        print()
        pre = i