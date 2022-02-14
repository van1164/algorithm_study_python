while True:
    try:
        lst= list(input())
        if lst ==[]:
            break
        check = [0,0,0,0]
        for i in lst:
            if 'a'<=i<='z':
                check[0]+=1
            elif 'A'<=i<='Z':
                check[1]+=1
            elif '0'<=i<='9':
                check[2]+=1
            else:
                check[3]+=1
        for i in check:
            print(i,end=' ')
        print()
    except EOFError:
        break