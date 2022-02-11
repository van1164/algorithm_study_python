a = int(input())
b =a
blue =0
white = 0
lst = []
for i in range(a):
    lst.append(list(map(int,input().rstrip().split())))
while(a>0):
    
    j = 0
    while(a+j<b+1):
        i = 0
        while(a+i<b+1):
            dic = {0:0,1:0,2:0,3:0}
            for k in range(j,a+j):
                for l in range(i,a+i):
                    dic[lst[k][l]]+=1
            if dic[0] == a*a:
                white +=1
                for k in range(j,a+j):
                    for l in range(i,a+i):
                        lst[k][l] = 2
            elif dic[1] ==a*a:
                blue+=1
                for k in range(j,a+j):
                    for l in range(i,a+i):
                        lst[k][l] = 3
            i+=a
        
        j+=a
    a = int(a//2)
print(white)
print(blue)