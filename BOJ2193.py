def fibo(n,visited):
    if visited[n] !=-1:
        return visited[n]
    else:
        visited[n] = fibo(n-1,visited)+fibo(n-2,visited)
        return visited[n] 


N =int(input())
visited =[-1 for _ in range(N+1)]
visited[0:3] =[1,1,1]
print(fibo(N,visited))