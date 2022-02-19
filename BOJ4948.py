def prime_number(number,visited):
    if number in visited:
        return False
    if number != 1:
        for f in range(2, int(number**(1/2))+1):  
            if number % f == 0:     
                return False    
    else:                       
        return False            
    return True

visited = {1}
for f in range(2, 123456*2+1):  
    if prime_number(f,visited):
        i =2
        while f*i<123456*2+1:
            visited.add(f*i)
            i+=1

while True:
    a= int(input())
    if a==0:
        break
    cnt=0
    for i in range(a+1,2*a+1):
        if i in visited:
            continue
        else:
            cnt+=1
    print(cnt)