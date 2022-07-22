string1 = input()
string2 = input()

N = len(string1)
M= len(string2)

graph = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        if string1[i] ==string2[j]:
            graph[i+1][j+1] = graph[i][j]+1
        else:
            graph[i+1][j+1] = max(graph[i][j+1], graph[i+1][j])

print(graph[-1][-1])
result = []
i =N
j = M
while i>0 and j>0:
    if string1[i-1]==string2[j-1]:
        result.append(string1[i-1])
        i-=1
        j-=1
    else:
        if graph[i][j] == graph[i-1][j]:
            i-=1
        else:
            j-=1
            
for i in range(graph[-1][-1]-1,-1,-1):
    print(result[i],end='')