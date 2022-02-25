def prime_number(number,visited):

    if not visited[number]:
        for f in range(2, int(number**(1/2))+1):  
            if number % f == 0:     
                return False    
    else:                       
        return False            
    return True

visited = [False]+[True]+[False]*10000000

a,b = list(map(int,input().split()))
maxx = 10000001
if b <maxx:
    maxx = b
else:
    b = maxx
for j in range(a,b+1):
    tmp = str(j)
    if tmp == tmp[::-1]:
        if prime_number(j,visited):
            print(j)
            k=2
            while k*j<=maxx:
                visited[k*j] =True
                k+=1
print(-1)
