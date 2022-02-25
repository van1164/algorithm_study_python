s = input()
a=[x for x in s.split('0') if x!= '']
b =[x for x in s.split('1') if x!= '']
if len(a)>=len(b):
    print(len(b))
else:
    print(len(a))
