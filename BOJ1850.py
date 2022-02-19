def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a




a,b = list(map(int,input().split()))
print('1'*(b-a))
