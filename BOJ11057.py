lst = [1,1,1,1,1,1,1,1,1,1]
a= int(input())
for i in range(a-1):
    for j in range(10):
        lst[j] = sum(lst[j:])%10007
print(sum(lst)%10007)