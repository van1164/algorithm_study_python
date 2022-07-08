import sys

N = int(sys.stdin.readline())
lst = dict()
for i in range(1,N+1):
    lst[i] = {x for x in range(1,N+1)}
for i in range(1,N+1):
    