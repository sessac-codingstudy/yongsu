#https://www.acmicpc.net/problem/27160

def HG():
    a = int(input())
    b = dict.fromkeys(['STRAWBERRY', 'BANANA', 'LIME', 'PLUM'], 0)
    for _ in range(a):
        c = input().split()
        b[c[0]] += int(c[1])
    for key, value in b.items():
        if value == 5:
            print('YES')
            return None
    print('NO')

HG()
