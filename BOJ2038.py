a= int(input())
dp ={1:1,2:2,3:2}
if a ==1:
    print(1)
    exit()
elif a ==2 or a==3:
    print(2)
    exit()
elif a == 4 or a==5:
    print(3)
    exit()
else:
    result = 5
    tmp = 4
    start =3
    while result <a:
        for i in range(dp[start]):
            dp[tmp] = start
            result+=start
            if result>=a:
                print(tmp)
                exit()
            tmp+=1
        del dp[start]
        start+=1
    print(tmp)