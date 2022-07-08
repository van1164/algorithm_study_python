a,b = input().split()
a_neg=False
b_neg =False
if a[0] =='-':
    a_neg =True
if b[0]=='-':
    b_neg = True
if a_neg and b_neg:
    a = a[1:]
    b = b[1:]
    x =sum_big(a,b)
    print('-',x,sep='')
elif a_neg:
    re_neg = False
    if int(a[1:])>=int(b):
        x= sub_big(a,b)
    else:
        x = sub_big(b,a)