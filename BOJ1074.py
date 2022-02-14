def recursive(n,start,end):
    if n[2] ==1:
        if start ==end:
            print(start[2])
            exit()
        elif [start[0]+1,start[1]] == end:
            print(start[2]+1)
            exit()
        elif [start[0],start[1]+1] == end:
            print(start[2]+2)
            exit()
        elif [start[0]+1,start[1]+1] == end:
            print( start[2]+3)
            exit()
        else:
            start[2] +=4
    else:
        for i in range(n[0],n[0]+2**n[2],2**(n[2]-1)):
            for j in range(n[1],n[1]+2**n[2],2**(n[2]-1)):
                start[0] = j
                start[1] = i
                recursive((i,j,n[2]-1),start,end)
    return start[2]


    
    
    
    
    
a,b,c = list(map(int,input().rstrip().split()))
print(recursive((0,0,a),[0,0,0],[b,c])-1)