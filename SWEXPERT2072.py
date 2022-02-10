a = int(input())
for i in range(a):
    lst = list(map(int,input().rstrip().split()))
    result = 0
    for j in lst:
        if j%2 !=0:
            result+=j
    print('#{} {}'.format(i+1,result))