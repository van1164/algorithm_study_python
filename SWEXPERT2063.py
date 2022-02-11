a = int(input())
lst = list(map(int,input().rstrip().split()))
lst.sort()
print(lst[a//2])