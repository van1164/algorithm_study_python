from itertools import combinations
a,b = list(map(int,input().split()))
one_lst =[]
two_lst = []
for i in range(a):
    lst = input().split()
    for j in range(a):
        if lst[j] =='1':
            one_lst.append((i,j))
        elif lst[j] =='2':
            two_lst.append((i,j))
tour_minn = 100000000000
for i in list(combinations(two_lst,b)):
    temp = 0
    for k in one_lst:
        minn = 100000000
        for j in i:
            minn=min(minn, abs(j[0]-k[0]) + abs(j[1]-k[1]))
        temp+=minn
    tour_minn =min(tour_minn,temp)
print(tour_minn)
        