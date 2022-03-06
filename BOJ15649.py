def recursive(n,finish,cnt = 0,visited = []):
    if cnt ==n:
        for i in visited:
            print(i,end=' ')
        print()
        return 0
    for i in range(1,finish+1):
        if i in visited:
            continue
        recursive(n,finish,cnt+1,visited +[i])

a,b = list(map(int,input().split()))
recursive(b,a)