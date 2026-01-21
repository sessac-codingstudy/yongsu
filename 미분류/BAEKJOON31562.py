#https://www.acmicpc.net/problem/31562

def song():
    a, b = map(int, input().split())
    c = {}
    for _ in range(a):
        d = input().split()
        c[d[1]] = d[2:5]
    for _ in range(b):
        e = input().split()
        f = []
        for key, value in c.items():
            if value == e:
                f.append(key)
        if len(f) == 1:
            print(f[0])
        elif len(f) > 1:
            print('?')
        else:
            print('!')

song()
