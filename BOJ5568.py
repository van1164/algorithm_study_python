
def recursive(graph,visited,length,finish,count = 1,string = '',temp = ''):

    for i in range(length):
        if str(i) not in temp :
            a = string +graph[i]
            b = graph[i]  + string
            if count == finish:
                if a not in visited:
                    visited.add(a)
                if b not in visited:
                    visited.add(b)    
            else:
                recursive(graph,visited,length,finish,count+1,a,temp +str(i))
                recursive(graph,visited,length,finish,count+1,b,temp+str(i))
        else:
            continue
    return visited


a = int(input())
b = int(input())
lst = []
sett = set()
for i in range(a):
    lst.append(input())
recursive(lst,sett,a,b)
print(len(sett))