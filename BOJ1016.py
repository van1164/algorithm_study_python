def prime_number(number,visited):
    if number in visited:
        return False
    else:
        for f in range(2, int(number**(1/2))+1):  
            if number % (f*f) == 0:     
                return False    
          
    return True

visited = set()
cnt = 0
a,b= list(map(int,input().split()))
for f in range(a,b+1):  
    if prime_number(f,visited):
        i =2
        cnt+=1
        while f*i<b+1:
            visited.add(f*i*i)
            i+=1

print(cnt)