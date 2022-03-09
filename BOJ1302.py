a = int(input())
dic = dict()
for i in range(a):
    sell = input()
    if sell in dic:
        dic[sell]+=1
    else:
        dic[sell] =1
maxx = 0
result = ''
for i in dic:
    if dic[i]>maxx:
        maxx =dic[i]
        result = i
    elif dic[i]==maxx:
        if result>i:
            result = i
            
print(result)