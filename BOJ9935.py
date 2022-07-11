S = input()
temp =[]
for i in S:
    temp.append(i)
S = temp
fire = input()
temp = []
for i in fire:
    temp.append(i)
fire =temp
end = fire[-1]
length = len(fire)
found = False
stack =[]
for i in range(len(S)):
    stack.append(S[i])
    if stack[-1]==end and len(stack)>=len(fire):
        if stack[-length:] == fire:
            for x in range(len(fire)):
                stack.pop()
if stack:
    for i in stack:
        print(i,end='') 
else:
    print("FRULA")   
