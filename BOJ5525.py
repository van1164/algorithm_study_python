a = int(input())
m = int(input())
s = input()
idx =0
result = 0
while(idx<len(s)):
    if s[idx] == 'I':
        if  idx+2<len(s) and s[idx+1] + s[idx+2] == 'OI':
            cnt = 0
            while idx+2<len(s) and s[idx+1] + s[idx+2] =='OI':
                cnt+=1
                idx+=2
            if cnt-a+1<=0:
                continue
            else:
                result+=cnt-a +1
        else: idx+=1
    else:
        idx+=1
print(result)