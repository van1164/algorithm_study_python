a,b = input().split()
b = int(b)
summ =0
length = len(a)
for i in range(length-1,-1,-1):
    if ord(a[length-i-1])<=57:
        summ+=(ord(a[length-i-1])-48)*pow(b,i)
    else:
        summ+=(ord(a[length-i-1])-55)*pow(b,i)
        
print(summ)