t = int(input())
for i in range(t):
    a= int(input())
    lst = []
    for _ in range(2):
        lst.append(list(map(int,input().split())))
    
    first = lst[0][0]
    second = lst[1][0]
    none = 0
    for j in range(1,a):
        x = max(first,second)
        y = max(second+lst[0][j],none+lst[0][j])
        z = max(first+lst[1][j],none+lst[1][j])
        none = x
        first =y
        second = z
    print(max(max(none,first),second))
    