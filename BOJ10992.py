a = int(input())
if a ==1:
    print('*')
else:
    print(' '*(a-1)+'*')
    for i in range(2,a):
        print(' '*(a-i) + '*'+' '*(2*i-3)+'*')
    print('*'*(2*a-1))