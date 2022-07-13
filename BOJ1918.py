from collections import deque
def gwal_mul(lst :deque):
    stack = deque([])
    while lst:
        p = lst.popleft()
        if p=='*'or p=='/':
            if stack[-1]==')':
                cnt = 0
                temp_stack =[]
                while True:
                    x = stack.pop()
                    if x =='(':
                        cnt-=1
                    elif x ==')':
                        cnt+=1
                    temp_stack.append(x)
                    if cnt ==0:
                        stack.append('(')
                        while temp_stack:
                            stack.append(temp_stack.pop())
                        break
            else:
                x = stack.pop()
                stack.append('(')
                stack.append(x)
            stack.append(p)
            next = lst.popleft()
            if next=='(':
                cnt = 1
                temp_go = deque([])
                temp_go.append(next)
                while lst:
                    next = lst.popleft()
                    if next == ')':
                        cnt-=1
                    elif next =='(':
                        cnt+=1
                    temp_go.append(next)
                    if cnt ==0:
                        stack+=gwal_mul(temp_go)
                        break
                stack.append(')')
            else:
                stack.append(next)
                stack.append(')')
        else:
            stack.append(p)

        
    return stack


def gwal_plus(lst :deque):
    stack = deque([])
    while lst:
        p = lst.popleft()
        if p=='+'or p=='-':
            if stack[-1]==')':
                cnt = 0
                temp_stack =[]
                while True:
                    x = stack.pop()
                    if x =='(':
                        cnt-=1
                    elif x ==')':
                        cnt+=1
                    temp_stack.append(x)
                    if cnt ==0:
                        stack.append('(')
                        while temp_stack:
                            stack.append(temp_stack.pop())
                        break
            else:
                x = stack.pop()
                stack.append('(')
                stack.append(x)
            stack.append(p)
            next = lst.popleft()
            if next=='(':
                cnt = 1
                temp_go = deque([])
                temp_go.append(next)
                while lst:
                    temp = lst.popleft()
                    if temp == ')':
                        cnt-=1
                    elif temp =='(':
                        cnt+=1
                    temp_go.append(temp)
                    if cnt ==0:
                        stack+=gwal_plus(temp_go)
                        break
                stack.append(')')
            else:
                stack.append(next)
                stack.append(')')
        else:
            stack.append(p)
        
    return stack


def rpx(lst):
    lst = gwal_mul(lst)
    lst = gwal_plus(lst)
    operand = []
    operator=[]
    
    while lst:
        x = lst.popleft()
        if x ==')' and operator:
            x = operator.pop()
            if x=='(':
                continue
            else:
                operand.append(x)
                temp_stack = deque([])
                while operator:
                    temp = operator.pop()
                    if temp =='(':
                        while temp_stack:
                            operator.append(temp_stack.popleft())
                        break
                    else:
                        temp_stack.append(temp)
                    
        elif x =='(':
            operator.append('(')
        elif x =='+'or x=='-' or x=='*'or x=='/':
            operator.append(x)
        else:
            operand.append(x)    
    while operator:
        x=operator.pop()
        if x !='(':
            operand.append(x)
    return operand    



string = input().strip()
lst = deque([])
for i in string:
    if i =='\n':
        continue
    lst.append(i)


for i in rpx(lst):
    print(i,end='')
print()