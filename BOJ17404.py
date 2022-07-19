import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))





#N == red
red = 100000000000
green = lst[0][1]
blue = lst[0][2]

for i in range(1,N-1):
    temp_red = min (green,blue)+lst[i][0]
    temp_green = min(red,blue)+lst[i][1]
    temp_blue = min(red,green)+lst[i][2]
    
    red = temp_red
    green = temp_green
    blue = temp_blue

red_minn = lst[-1][0] + min(green,blue)

#N == green
red = lst[0][0]
green = 10000000000
blue = lst[0][2]

for i in range(1,N-1):
    temp_red = min (green,blue)+lst[i][0]
    temp_green = min(red,blue)+lst[i][1]
    temp_blue = min(red,green)+lst[i][2]
    
    red = temp_red
    green = temp_green
    blue = temp_blue

green_minn = lst[-1][1] + min(red,blue)

#N == blue
red = lst[0][0]
green = lst[0][1]
blue = 1000000000000

for i in range(1,N-1):
    temp_red = min (green,blue)+lst[i][0]
    temp_green = min(red,blue)+lst[i][1]
    temp_blue = min(red,green)+lst[i][2]
    
    red = temp_red
    green = temp_green
    blue = temp_blue

blue_minn = lst[-1][2] + min(red,green)

print(min(red_minn,green_minn,blue_minn))
