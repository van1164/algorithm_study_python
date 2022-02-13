result ='I'
a = int(input())
result = result + 'OI'*a
m = int(input())
s = input()
cnt = 0
while(s.find('I')!=-1):
    x = s.find('I')
    s= s[s.find(result)+2:]
    cnt+=1
print(cnt)