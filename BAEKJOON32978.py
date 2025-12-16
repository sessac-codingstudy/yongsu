#https://www.acmicpc.net/problem/32978

def get_input():
    a = input()
    b = input().split()
    c = input().split()
    return a, b, c

def marneul():
    a, b, c = get_input()
    d = dict.fromkeys(b, 0)
    for x in c:
        d[x] = 1
    for key, value in d.items():
        if value == 0:
            print(key)

marneul()
