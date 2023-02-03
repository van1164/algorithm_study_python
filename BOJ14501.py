import sys
t = int(sys.stdin.readline())
time_graph =[0]
coin_graph =[0]
graph = [0]*(t+1)

for i in range(t):
    a,b = list(map(int,sys.stdin.readline().split()))
    time_graph.append(a)
    coin_graph.append(b)
    
for i in range(1,t+1):
    print(i,graph)
    if i+time_graph[i]-1<=t:
        graph[i+time_graph[i]-1] = max(graph[i+time_graph[i]-1],graph[i],graph[i-1]+coin_graph[i])
    else:
        graph[i]=max(graph[i],graph[i-1])
        
print(graph)
    
    