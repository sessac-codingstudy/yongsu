N = int(input())
coor = list(map(int,input().split()))
unique = list(set(coor))
unique.sort()
index = {}
# for num in coor:
#     print(unique.index(num), end=" ")
for i, x in enumerate(unique):
    index[x] = i
for num in coor:
    print(index[num], end=' ')