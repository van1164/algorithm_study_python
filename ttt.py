a,b =list(map(int,input().split()))
summ_a =0
summ_b = 0
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
lst =sorted(lst)
for i in lst:
    summ_a +=i[0]
    summ_b+=i[1]
    print(summ_a,summ_b)
print(summ_a,summ_b)