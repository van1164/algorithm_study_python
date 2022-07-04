import sys
sys.setrecursionlimit(10 ** 9)
visited = {'0':0,'1':1,'2':1}

def fibo(n):
    print(n)
    if str(n) in visited:
        return visited[str(n)]
    else:
        visited[str(n)] = (fibo(n-1)+fibo(n-2))%1000000007
        del visited[str(n-2)]
        return visited[str(n)]
    
    
a = int(input())
print(fibo(a))
