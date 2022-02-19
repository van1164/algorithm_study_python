def fibo(n, visited={0:0,1:1}):
    if n in visited:
        return visited[n]
    else:
        visited[n] = fibo(n-1)+fibo(n-2)
        return visited[n]
a=int(input())
print(fibo(a))