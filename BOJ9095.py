a = int(input())
dic = {1:{'1'},2:{'11','2'},3:{'111','12','21','3'}}
for i in range(4,11):
    dic[i] = set()
for i in range(4,11):
    for j in range(1,int(i/2)+1):
        for k in dic[j]:
            for l in dic[i-j]:
                dic[i].add(k+l)
                dic[i].add(l+k)
for i in range(a):
    x = int(input())
    print(len(dic[x]))