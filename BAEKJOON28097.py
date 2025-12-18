# https://www.acmicpc.net/problem/28097

# 문제는 끝까지 읽도록 하자.
# 마지막 함수 호출도 잊지 말자.

def study_time():
    study_counts = int(input())
    study_time = map(int, input().split())
    total_time = (study_counts-1)*8
    for time in study_time:
        total_time += time
    print(total_time//24, total_time%24)
    
study_time()
