visited = {0:(1,0),1:(0,1)}

def fibonacci(n) :
    if n == 0:
        return (1,0)
    elif n ==1:
        return (0,1)
    if n in visited:
        return visited[n]
    else:
        x = fibonacci(n-1)
        y= fibonacci(n-2)
        visited[n] = (x[0]+y[0],x[1]+y[1])
        return visited[n]
t = int(input())
for i in range(t):
    x = int(input())
    a = fibonacci(x)
    print(a[0],a[1])
    