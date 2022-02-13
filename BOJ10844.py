lst = [0,1,1,1,1,1,1,1,1,1]
a= int(input())
for i in range(a-1):
    tmp = lst[:]
    for j in range(10):
        if j ==0 or j ==9:
            continue
        else:
            lst[j]= tmp[j-1]+tmp[j+1]
    lst[0]=tmp[1]
    lst[9]=tmp[8]
print(sum(lst)%1000000000)