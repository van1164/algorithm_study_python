import sys

N= int(sys.stdin.readline().rstrip())
M= int(sys.stdin.readline().rstrip())

visited = [False]*(N+1)

for i in range(M):
    visited[int(sys.stdin.readline().rstrip())]=True
print(visited.count(True))
    