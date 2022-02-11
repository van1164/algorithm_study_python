a = int(input().rstrip())
for i in range(a):
    a,b = list(map(int,input().rstrip().split()))
    if a>b:
        print("#{} {}".format(i+1,">"))
    elif a<b:
        print("#{} {}".format(i+1,"<"))
    else:
        print("#{} {}".format(i+1,"="))