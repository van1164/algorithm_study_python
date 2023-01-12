import sys

input =sys.stdin.readline

t = int(input())
lst = []
for _ in range(t):
    lst.append(int(input()))
    
zero_dp =[0]
one_dp=[0]
two_dp =[0]

for i in range(t):
    zero=max(zero_dp[-1],one_dp[-1],two_dp[-1])
    one = zero_dp[-1]+lst[i]
    two = one_dp[-1]+lst[i]
    zero_dp.append(zero)
    one_dp.append(one)
    two_dp.append(two)
    
print(max(zero_dp[-1],one_dp[-1],two_dp[-1]))