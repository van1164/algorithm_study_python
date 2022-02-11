from itertools import product
number = input()
num = int(number)
kt = list(map(int,list(number)))
a = int(input())
if a != 0:
    lst = set(input().rstrip().split())
else:
    lst = set()
minn = abs(100 - num)
lst = {'1','2','3','4','5','6','7','8','9','0'} - lst

x = 600000
length = 0
for i in product(lst,repeat = len(kt)):
    if x>abs(num-int("".join(i)))+len("".join(i)):
        x = abs(num-int("".join(i)))+len("".join(i))
for i in product(lst,repeat = len(kt)-1):
    if "".join(i) == '':
        break
    if x>abs(num-int("".join(i)))+len("".join(i)):
        x = abs(num-int("".join(i)))+len("".join(i))
for i in product(lst,repeat = len(kt)+1):
    if x>abs(num-int("".join(i)))+len("".join(i)):
        x = abs(num-int("".join(i)))+len("".join(i))
if x<minn:
    print(x)
else:
    print(minn)