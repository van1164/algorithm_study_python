string = input()
pop = input()

while pop in string:
    string = "".join(string.split(pop))
if string:
    print(string)
else:
    print("FRULA")