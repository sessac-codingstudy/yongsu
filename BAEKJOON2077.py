# https://www.acmicpc.net/problem/2077

# 아래는 내가 적은 코드긴 한데 메모리초과로 오답.
# 배운점
# 문자열 합치기는 메모리적으로 비효율적이다. str1 += str2 대신, 리스트에 .append로 합칠것들을 다 때려박고 "".join(result)를 하는 것이 훨씬 메모리절감됨.
# 리스트 슬라이싱은 나쁘진 않은데 슬라이스 할 크기가 적다면(ex:3) [i:i+3] 보다는, a = li[i], b = li[i+1], c= li[i+2] 로 변수에 할당하여 비교하는 것이 메모리절감됨.

def ore():
    cases = int(input())
    for _ in range(cases):
        length = int(input())
        mine = list(map(int, input().split()))
        support = 0
        disabled = 0
        result = []
        while length - support >= 6:
            size3 = mine[support+4]
            size2 = mine[support+3]
            size1 = mine[support+2]
            if size3 <= size2 and size3 <= size1:
                result.append('0333')
                support += 4
                disabled += mine[support]
            elif size2 <= size1:
                result.append('022')
                support += 3
                disabled += mine[support]
            else:
                result.append('01')
                support += 2
                disabled += mine[support]
        if length - support == 5:
            if mine[support+3] >= mine[support+2]:
                result.append('01022')
                disabled += mine[support+2]
            else:
                result.append('02201')
                disabled += mine[support+3]
        elif length - support == 4:
            result.append('0333')
        elif length - support == 3:
            result.append('022')
        elif length - support == 2:
            result.append('01')
        if disabled <= 0.25 * sum(mine):
            print("YES")
            print("".join(result))
        else:
            print("NO")

ore()
