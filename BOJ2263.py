import sys
sys.setrecursionlimit(10**9)
a = int(input())
lst = list(map(int,sys.stdin.readline().split()))
graph =  list(map(int,sys.stdin.readline().split()))
inidx = [0]*1000001
for i, node in enumerate(lst):
    inidx[node] = i
def recur(start,end,g_start,g_end):
    if g_start<g_end and start<end and start>=0 and g_start>=0:
        mid = inidx[graph[g_end-1]]
        print(lst[mid],end=' ')
        mid = mid-start
        recur(start,start+mid,g_start,g_start+(mid))
        recur(start+mid+1,end,g_start+(mid),g_end-1)
            


recur(0,a,0,a)

