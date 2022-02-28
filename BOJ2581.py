def prime_number(number,visited):

    if not visited[number]:
        for f in range(2, int(number**(1/2))+1):  
            if number % f == 0:     
                return False    
    else:                       
        return False            
    return True

visited = [False]+[True]+[False]*10000000

a= int(input())
b = int(input())
minn = 10001
summ =0
for j in range(a,b+1):
    if prime_number(j,visited):
        if minn == 10001 and minn>j:
            minn = j
        summ +=j
        k=2
        while k*j<=minn:
            visited[k*j] =True
            k+=1
if minn ==10001:
    print(-1)
else:
    print(summ)
    print(minn)
