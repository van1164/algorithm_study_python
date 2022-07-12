from collections import deque
stack = []
temp = deque([])
string = input()
for i in string:
    temp.append(i)
temp_stack = []
while temp:
    x = temp.popleft()
    if x== '<':
        while temp_stack:
            stack.append(temp_stack.pop())
        stack.append('<')
        while True:
            tmp = temp.popleft()
            stack.append(tmp)
            if tmp =='>':
                break
    elif x ==' ':
        while temp_stack:
            stack.append(temp_stack.pop())
        stack.append(' ')
    else:
        temp_stack.append(x)

while temp_stack:
    stack.append(temp_stack.pop())
print("".join(stack))