a = int(input())
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
for i in range(a-2,-1,-1):
    for j in range(len(lst[i])):
        lst[i][j] +=max(lst[i+1][j],lst[i+1][j+1])
print(lst[0][0])