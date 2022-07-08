import sys
from itertools import combinations
tc = int(sys.stdin.readline())

for _ in range(tc):
    V,E = list(map(int,sys.stdin.readline().split()))
    graph = [[] for _ in range(V+1)]
    visited = set()
    for _ in range(E):
        G,F = list(map(int,sys.stdin.readline().split()))
        graph[G].append(F)
        graph[F].append(G)
    boo =True
    for x,y in combinations(range(1,V+1),2):
        if graph[x]==graph[y] and len(graph[x])==V-2:
            print("YES")
            boo = False
            break
    if boo:
        print("NO")
        
        