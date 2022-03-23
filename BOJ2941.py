string = input()
length  = len(string)
cnt = 0
i = -1
while(i<length-1):
    i+=1
    tmp = string[i]
    if tmp =='c' and i<length-1:
        if string[i+1]=='=' or string[i+1]=='-':
            cnt+=1
            i+=1
        else:
            cnt+=1
    elif tmp == 'd':
        if i<length-1 and string[i+1]=='-' :
            cnt+=1
            i+=1
        elif i<length-2 and string[i+1]=='z' and string[i+2]=='=':
            cnt+=1
            i+=2
        else:
            cnt+=1
    elif (tmp == 'l' or tmp == 'n')and i<length-1:
        if string[i+1]=='j':
            cnt+=1
            i+=1
        else:
            cnt+=1
    elif (tmp =='s' or tmp == 'z')and i<length-1:
        if string[i+1]=='=':
            cnt+=1
            i+=1
        else:
            cnt+=1
    else:
        cnt+=1
print(cnt)