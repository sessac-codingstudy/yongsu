def sorter(num):
    num = str(num)
    index = {9:0, 8:0, 7:0, 6:0, 5:0,
             4:0, 3:0, 2:0, 1:0, 0:0}
    result = []
    for chr in num:
        index[int(chr)] += 1
    for key, value in index.items():
        for _ in range(value):
            result.append(key)
    return int("".join(map(str, result)))

print(sorter(input()))