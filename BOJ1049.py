import math


a,b = list(map(int,input().split()))
package_minn = 100000000
item_minn =1000000000
for i in range(b):
    x,y = list(map(int,input().split()))
    package_minn = min(x,package_minn)
    item_minn = min(y,item_minn)
print(min(item_minn *a,package_minn*math.ceil(a/6), package_minn*(a//6)+item_minn*(a%6)))