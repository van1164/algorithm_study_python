import sys
a = int(input())


for i in range(a):
    x = int(input())
    dic = {}
    for j in range(x):
        a,b = sys.stdin.readline().rstrip().split()
        if b in dic:
            dic[b].append(a)
        else:
            dic[b]=[a]
    result = 1
    for k in dic:
        result*=(len(dic[k])+1)
    print(result-1)
