import sys
lst = [False]*31
for i in range(28):
    a = int(sys.stdin.readline())
    lst[a] = True
    
for i in range(1,31):
    if not lst[i]:
        print(i)