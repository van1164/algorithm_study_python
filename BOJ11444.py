def fibo(n,visited = {1:1,2:1}):
    n = n%1000000007
    print(n)
    if n in visited:
        return visited[n]
    else:
        visited[n] = (fibo(n-1,visited)+fibo(n-2,visited))%1000000007
        return visited[n]
    
    
a = int(input())
print(fibo(a))
