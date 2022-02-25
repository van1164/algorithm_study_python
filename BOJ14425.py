a,b=list(map(int,input().split()))
sett = set()
cnt = 0
for i in range(a):
    sett.add(input())
for i in range(b):
    x = input()
    if x in sett:
        cnt+=1
print(cnt)