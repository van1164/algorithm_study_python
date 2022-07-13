from math import gcd

a,b  = list(map(int,input().split(':')))
x = gcd(a,b)

print(a//x,':',b//x,sep='')