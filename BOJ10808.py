lst = [0]*26
string= input().rstrip()
for i in string:
    lst[ord(i)-ord('a')]+=1
for i in lst:
    print(i,end=' ')