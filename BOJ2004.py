a,b = list(map(int,input().split()))
if a-b<b:
    b = a-b
cnt_2_1 = 0
cnt_5_1 = 0
cnt_2_2 = 0
cnt_5_2 = 0
t=1
p =1
for i in range(b):
    t *=a
    a-=1
    
while t%2 == 0:
    t= t//2
    cnt_2_1+=1
while t%5 == 0:
    t=t//5
    cnt_5_1+=1

for i in range(b,0,-1):
    p *=i
while p%2 == 0:
    p= p//2
    cnt_2_2+=1
while t%5 == 0:
    t=t//5
    cnt_5_2+=1

print(min(cnt_2_1 - cnt_2_2,cnt_5_1-cnt_5_2))