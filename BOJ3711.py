import sys
t = int(sys.stdin.readline())
for i in range(t):
    count = int(sys.stdin.readline())
    lst = []
    for j in range(count):
        lst . append(int(sys.stdin.readline()))
    visited = set()
    i =1
    while True:
        boo = True
        for k in lst:
            if k%i in visited:
                i+=1
                boo = False
                break
            else:
                visited.add(k%i)
                continue
        if boo:
            print(i)
            break
        