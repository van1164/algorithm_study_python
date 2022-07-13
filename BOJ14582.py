lst = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

many = False
sum1 =0
sum2 = 0
for i in range(9):
    sum1+=lst[i]
    if sum1>sum2:
        many =True
    sum2+=lst2[i]
if many:
    print("Yes")
else:
    print("No")