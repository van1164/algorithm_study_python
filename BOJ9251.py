a = input()
b = input()
maxx = 0
lst = [[0]*(len(b)+1)]
for i in range(len(a)):
    tmp = [0]
    for j in range(len(b)):
        if a[i] == b[j]:
            tmp.append(lst[i][j]+1)
            if maxx<lst[i][j]+1:
                maxx =lst[i][j]+1
        else:
            tmp.append(max(tmp[-1],lst[i][j+1]))
    lst.append(tmp)

print(maxx)
