a= int(input())
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
r=lst[0][0]
g =lst[0][1]
b =lst[0][2]

for i in range(1,a):
    x =min(g,b)
    y = min(r,b)
    z = min(g,r)
    r=x+lst[i][0]
    g = y+lst[i][1]
    b=z+lst[i][2]
print(min(min(r,g),b))

