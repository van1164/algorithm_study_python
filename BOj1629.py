def fpow(C, n,mod):
	if n == 1:
		return C % mod
	else:
		x = fpow(C, n//2,mod)
		if n % 2 == 0:
			return (x * x)%mod 
		else:
			return (x * x * C)%mod

a,b,c = list(map(int,input().split()))
print(fpow(a,b,c))