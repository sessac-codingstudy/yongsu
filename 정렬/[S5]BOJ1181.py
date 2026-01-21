#https://www.acmicpc.net/problem/1181

#정렬에 대한 새로운 테크닉을 배워서 적어봄. 아래의 gemini(N)함수 참고
#리스트에 대한 .sort()메서드가 있는데, 기똥찬 기능이 하나 있다.
#인자로 key=function을 넣는건데, pandas에서 df.apply()와 비슷하다.
#근데 특이하게, function의 반환값이 "튜플"일 경우,
#해당 반환 튜플의 "앞"기준으로 먼저 정렬하고,
#"앞"기준에서 동일할 경우 그 다음 "뒷"기준으로 정렬한다.

#효율성 측면
#.sort(key=function)는 시간적인 측면에선 리스트 한번 훑는 정도밖에 소모하지 않는다.
#다만, 메모리는 원본리스트 1개분량만큼 더 소모하므로 메모리제한에는 유의하자.

import sys
def input():return sys.stdin.readline().rstrip()

def sorter(N):

    sorter1 = set()
    sorter2 = {}
    result = []

    # input받아서 set으로 저장
    for _ in range(N):
        sorter1.add(input())

    # 받은 문자열들을 딕셔너리에 저장
    # 이 때, key값이 문자열 길이가 된다.
    # 예시 = {
    #     1:["i", "a"],
    #     2:["am", "to"],
    #     3:["are", "boy"],
    #     4:["home"],
    #     8:["hesitate"]
    # }
    for item in sorter1:
        if len(item) in sorter2:
            sorter2[len(item)].append(item)
        else:
            sorter2[len(item)] = [item]

    # 만든 딕셔너리(sorter2)를 문자열 길이 오름차순으로 정렬한다.
    sorter2 = sorted(sorter2.items())

    # 문자열 길이 오름차순으로 정렬된 리스트들을
    # 리스트 자체 내부에서 문자열 오름차순으로 정렬한 뒤
    # result 리스트에 순서대로 넣는다.
    for key, item in sorter2:
        item.sort()
        result += item

    # 순서대로 프린트하여 완료
    for x in result:
        print(x)

sorter(int(input()))

# gemini의 최적해법
def gemini(N):
    word_set = set(input().strip() for _ in range(N))
    word_list = list(word_set)
    word_list.sort(key=lambda x: (len(x), x)) # 여기가 핵심
    for word in word_list:
        print(word)