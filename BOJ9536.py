import sys
t = int(input())

for i in range(t):
    result = sys.stdin.readline().split()
    while True:
        test = sys.stdin.readline()
        if test == "what does the fox say?\n":
            break
        else:
            x = test.split()[2]
            while x in result:
                result.remove(x)
    for i in result:
        print(i,end=' ')        
            
            