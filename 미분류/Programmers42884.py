#https://school.programmers.co.kr/learn/courses/30/lessons/42884

#작동방식은 옳았으나, 시간초과로 오답처리됨. 코딩테스트 방향성 재조정 필요
#https://www.youtube.com/watch?v=iWJUA78Fb8c 참고

import numpy as np

def solution(routes):
    cams = 0
    movements = np.array(routes) + 30000
    data = np.zeros((len(routes),60001), dtype=np.int8)
    for i, x in enumerate(movements):
        data[i,x[0]:(x[1]+1)] += 1
    while True:
        passes = np.sum(data,axis=0)
        if np.max(passes) == 0:
            break
        busy = np.argmax(passes)
        data[data[:,busy] == 1] = 0
        cams += 1
    return cams
