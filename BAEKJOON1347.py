# https://www.acmicpc.net/problem/1347

# 실버문제는 메모리할당도 넉넉하고 창의력도 요구하지 않는 듯 하다. 차근차근 코딩만 하면 정답처리됨.
# 제미나이 시켜봤는데 코드 9줄컷남 벽느껴짐

def maze():
    orders = int(input())
    movements = input()
    currentx = 0
    currenty = 0
    position = 0
    direction = [[0,-1],[-1,0],[0,1],[1,0]]
    mapping = {0:[0]}
    for chr in movements:
        if chr == 'R':
            position += 1
            if position == 4:
                position = 0
        elif chr == 'L':
            position -= 1
            if position == -1:
                position = 3
        else:
            currentx += direction[position][0]
            currenty += direction[position][1]
            mapping[currenty] = mapping.get(currenty, []) + [currentx]

    sizey = 0
    xcounter = []
    for x in mapping.values():
        xcounter += x
        sizey += 1
    sizex = list(dict.fromkeys(xcounter))
    minx = min(sizex)
    sizex = len(sizex)

    ydrawer = list(mapping.keys())
    ydrawer.sort(reverse=True)
    for x in ydrawer:
        current_line = mapping[x]
        point = minx
        xdrawer = ""
        for _ in range(sizex):
            if point in current_line:
                xdrawer += '.'
            else:
                xdrawer += '#'
            point += 1
        print(xdrawer)

maze()
