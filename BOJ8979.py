import sys


N,K = list(map(int,sys.stdin.readline().split()))
gold = [-1]*(N+1)
silver = [-1]*(N+1)
bronze = [-1]*(N+1)
for i in range(N):
    t,a,b,c =list(map(int,sys.stdin.readline().split()))
    gold[t] =a
    silver[t] =b
    bronze[t]=c
cnt = 0
one = gold[K]
two = silver[K]
three = bronze[K]
next = []
for i in range(N+1):
    if gold[i]>one:
        cnt+=1
    elif gold[i] == one:
        next.append(i)

third = []
for j in next:
    if silver[j]>two:
        cnt+=1
    elif silver[j]==two:
        third.append(j)

for k in third:
    if bronze[k]>three:
        cnt+=1
print(cnt+1)