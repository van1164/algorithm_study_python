def prime_number(number,visited):

    if number not in visited:
        for f in range(2, int(number**(1/2))+1):  
            if number % f == 0:     
                return False    
    else:                       
        return False            
    return True
t= int(input())
visited = {1}
for i in range(t):
    a = int(input())
    for j in range(a//2,0,-1):
        if prime_number(j,visited):
            if prime_number(a-j,visited):
                print(j,a-j,sep=' ')
                break
            k=2
            while k*j<=10000:
                visited.add(k*j)
                k+=1
        
