from collections import deque
a = int(input())
result = []
string =''
for i in range(a):
    result.append(int(input()))
stack = deque([x for x in range(1,a+1)])
middle  = deque()
lst = []
start = 0
for i in result:
    if i >start:
        for _ in range(i-start):
            middle.append(stack.popleft())
            string+='+'
        start = i
        middle.pop()
        string+='-'
    else:
        n = middle.pop()
        if n ==i:
            string+='-'
        else:
            print("NO")
            exit()
for i in string:
    print(i)