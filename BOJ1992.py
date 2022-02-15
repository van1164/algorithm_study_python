from math import log2


def recursive(graph,start,n,string=''):
    init = graph[start[0]][start[1]]
    if n==1:
        tmp = graph[start[0]][start[1]]+graph[start[0]][start[1]+1]+graph[start[0]+1][start[1]]+graph[start[0]+1][start[1]+1]
        if tmp =='1111':
            string+='1'
        elif tmp == '0000':
            string +='0'
        else:
            string +='('+tmp+')'
        return string
    tmp = ''
    for i in range(start[0],start[0]+2**n,2**(n-1)):
        for j in range(start[1],start[1]+2**n,2**(n-1)):
            tmp+= recursive(graph,[i,j],n-1,string)
    if tmp =='1111':
        string+='1'
    elif tmp == '0000':
        string +='0'
    else:
        string +='('+tmp+')'            
    
    return string


    
a = int(input())
lst = []
for i in range(a):
    lst.append(list(input().rstrip()))
print(recursive(lst,[0,0],int(log2(a))))