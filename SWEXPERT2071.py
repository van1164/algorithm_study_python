a = int(input().rstrip())
for i in range(a):
    lst = list(map(int,input().rstrip().split()))
    print("#{} {}".format(i+1,int(round(sum(lst)/len(lst)))))