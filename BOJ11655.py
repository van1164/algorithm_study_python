string = input().rstrip()
result = ''
for i in string:
    if 'a'<=i<'n':
        result+=chr(ord(i)+13)
    elif 'm'<i<='z':
        result+=chr(ord(i)-13)
    elif 'A'<=i<'N':
        result+=chr(ord(i)+13)
    elif 'M'<i<='Z':
        result+=chr(ord(i)-13)
    else:
        result+=i
print(result)