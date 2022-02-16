a,b =list(map(int,input().split()))
lst = []
bw = ['W','B']
for i in range(a):
    lst.append(list(input()))
minn =100000000
for i in range(0,a-7):
    for j in range(0,b-7):
        tmp = []
        cnt = 0
        for k in range(i,i+8):
            tmp.append(lst[k][j:j+8])
        start1 =0
        start2 =1
        cnt_1=0
        cnt_2 = 0
        for k in range(len(tmp)):
            start1= (start1+1)%2
            start2 =(start2+1)%2
            for l in range(len(tmp)):
                if tmp[k][l] == bw[start1]:
                    cnt_1+=1
                    start1= (start1+1)%2
                else:
                    start1= (start1+1)%2
                if tmp[k][l] == bw[start2]:
                    cnt_2+=1
                    start2 =(start2+1)%2
                else:
                    start2= (start2+1)%2
        if minn>min(cnt_1,cnt_2):
            minn = min(cnt_1,cnt_2)
                    
print(minn)