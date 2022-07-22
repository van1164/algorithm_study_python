N=int(input())
if N==1:
    print(0)
    print(1)
    exit()
one = [0]*(N+1)
two = [0]*(N+1)
three= [0]*(N+1)

if N%3==0:
    three[N//3] =1
if N%2 ==0:
    two[N//2]=1
if N-1>0:
    one[N-1]=1


for i in range(N,0,-1):
    if one[i]!=0:
        if i %3 ==0:
            if three[i//3] != 0 and three[i//3]>one[i]+1:
                three[i//3] = one[i]+1
            elif three[i//3]==0:
                three[i//3] = one[i]+1
        
        if i%2 ==0:
            if two[i//2] !=0 and two[i//2]>one[i]+1:
                two[i//2] = one[i]+1
            elif two[i//2]==0:
                two[i//2] = one[i]+1
        
        if i-1 >0:
            if one[i-1] !=0 and one[i-1] > one[i]+1:
                one[i-1] = one[i]+1
            elif one[i-1]==0:
                one[i-1] = one[i]+1
        
        
    if two[i]!=0:
        if i %3 ==0:
            if three[i//3] != 0 and three[i//3]>two[i]+1:
                three[i//3] = two[i]+1
            elif three[i//3]==0:
                three[i//3] = two[i]+1
        
        if i%2 ==0:
            if two[i//2] !=0 and two[i//2]>two[i]+1:
                two[i//2] = two[i]+1
            elif two[i//2]==0:
                two[i//2] = two[i]+1
        
        if i-1 >0:
            if one[i-1] !=0 and one[i-1] > two[i]+1:
                one[i-1] = two[i]+1
            elif one[i-1]==0:
                one[i-1] = two[i]+1
                
    if three[i]!=0:
        if i %3 ==0:
            if three[i//3] != 0 and three[i//3]>three[i]+1:
                three[i//3] = three[i]+1
            elif three[i//3]==0:
                three[i//3] = three[i]+1
        
        if i%2 ==0:
            if two[i//2] !=0 and two[i//2]>three[i]+1:
                two[i//2] = three[i]+1
            elif two[i//2]==0:
                two[i//2] = three[i]+1
        
        if i-1 >0:
            if one[i-1] !=0 and one[i-1] > three[i]+1:
                one[i-1] = three[i]+1
            elif one[i-1]==0:
                one[i-1] = three[i]+1

if one[1]==0:
    one[1]=1000000000
if two[1]==0:
    two[1]=1000000000
if three [1] == 0:
    three [1] = 10000000000
minn = min(one[1],two[1],three[1])
print(minn)
start = 0
if minn ==three[1]:
    start = 3
elif minn == two[1]:
    start=2
else:
    start =1
num =minn
i =1
result = []
while num>0:
    if start ==3:
        if three[i*3] == num-1:
            result.append(i)
            num-=1
            i=i*3
            start = 3
        elif two[i*3] == num-1:
            result.append(i)
            num-=1
            i=i*3
            start =2
        elif one[i*3] == num-1:
            result.append(i)
            num-=1
            i = i*3
            start=1
    elif start ==2:
        if three[i*2] == num-1:
            result.append(i)
            num-=1
            i=i*2
            start = 3
        elif two[i*2] == num-1:
            result.append(i)
            num-=1
            i=i*2
            start =2
        elif one[i*2] == num-1:
            result.append(i)
            num-=1
            i = i*2
            start=1
    elif start ==1:
        if three[i+1] == num-1:
            result.append(i)
            num-=1
            i=i+1
            start = 3
        elif two[i+1] == num-1:
            result.append(i)
            num-=1
            i=i+1
            start =2
        elif one[i+1] == num-1:
            result.append(i)
            num-=1
            i = i+1
            start=1
print(N,end=' ')
for i in range(len(result)-1,-1,-1):
    print(result[i],end=' ')