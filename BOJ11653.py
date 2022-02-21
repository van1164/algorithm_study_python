a= int(input())
i=2
while a>1:
    if a %i ==0:
        a=a//i
        print(i)
    else:
        i+=1