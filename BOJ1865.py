import sys

def bellman_ford(doro,N):
    distance= dict()
    for node in range(1,N+1):
        distance[node]=1000000000
    distance[1] = 0
    for i in range(N-1):
        for node in range(1,N+1):
            for n,time in doro[node]:
                if distance[n]>distance[node]+time:
                    distance[n]=distance[node]+time
    for node in range(1,N+1):
        for n,time in doro[node]:
            if distance[n]>distance[node]+time:
                return -1
    return 1

tc = int(input())
for _ in range(tc):
    N,M,W = list(map(int,sys.stdin.readline().split()))
    doro = [[] for _ in range(N+1)]
    for _ in range(M):
        S,E,T = list(map(int,sys.stdin.readline().split()))
        doro[S].append([E,T])
        doro[E].append([S,T])
    for _ in range(W):
        S,E,T = list(map(int,sys.stdin.readline().split()))
        doro[S].append([E,-T])
    if bellman_ford(doro,N)<0:
        print("YES")
    else:
        print("NO")