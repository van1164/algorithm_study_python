a = input()
if len(a)%3 ==0 :
    pass
elif len(a)%3 ==1:
    a='00'+a    
else:
    a = '0'+a
k = 0
result = ''
for i in range(0,len(a),3):
    tmp = 0
    if a[i]=='1':
        tmp +=4
    if a[i+1]=='1':
        tmp+=2
    if a[i+2] == '1':
        tmp+=1
    result += oct(tmp)[2:]

print(result)