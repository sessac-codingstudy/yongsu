# https://www.acmicpc.net/problem/25419

# DP를 처음으로 적용해서 풀어보았다.

def intgame():
    n, k = map(int,input().split())
    disabled_int = set(map(int,input().split()))
    places_holder = [0] * n
    for i in range(n-1,-1,-1):
        if i+1 in disabled_int:
            continue
        else:
            places_holder[i] = 1
            break
    if 1 not in places_holder:
        print(0)
        return
    for i in range(n-1,-1,-1):
        if i+1 in disabled_int:
            continue
        safe_step = 1
        for j in range(i+1,i+k+1):
            if j>n-1:
                break
            if places_holder[j] == 1:
                safe_step = 0
                break
        places_holder[i] = safe_step
    for i in range(0,k):
        if places_holder[i] == 1:
            print(1)
            return
    print(0)

intgame()
