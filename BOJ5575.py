for i in range(3):
    result = [0,0,0]
    lst = list(map(int,input().rstrip().split()))
    if lst[5]-lst[2]<0:
        result[1]-=1
        result[2] += lst[5]-lst[2]+60
    else:
        result[2] += lst[5]-lst[2]
    if lst[4]-lst[1]+result[1]<0:
        result[0]-=1
        result[1] += lst[4]-lst[1]+60
    else:
        result[1] += lst[4]-lst[1]
    result[0]+= lst[3]-lst[0]


    for k in result:
        print(k,end=' ')
    print()