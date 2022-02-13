dp = [0,1,2,3]
a = int(input())
for i in range(4,a+1):
    minn = 15
    for j in range(int(i**(0.5)),1,-1):
        tmp = i
        cnt =0
        if tmp - j**2 <0:
            continue
        elif tmp - j**2 ==0:
            cnt=1
            minn = cnt
            break
        else:
            cnt = dp[tmp - j**2]+1
            if cnt<minn:
                minn = cnt
    dp.append(minn)
        
print(dp[a])