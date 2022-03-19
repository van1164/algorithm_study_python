a, b = list(map(int,input().split()))
dp = {0:0}
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
lst = sorted(lst,key=lambda x:x[0])
for i in lst:
    if i[0] >b:
        break
    for j,k in list(dp.items()):
        if j + i[0]>b:
            continue
        else:
            if j +i[0] not in dp:
                dp[j+i[0]] = k+i[1]
            else:
                if dp[j+i[0]] < k+i[1]:
                    dp[j+i[0]] = k+i[1]                 
print(max(dp.values()))