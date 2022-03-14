a,b,c = list(map(int,input().split()))
result  =0
for i in range(c+1):
    woman = a -i
    man = b - (c-i)
    result = max(result,min(woman//2,man))
    
print(result)