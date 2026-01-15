#https://www.acmicpc.net/problem/17478

#재귀문제 easy난이도. 1트만에정답
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

def tap(m):
    print('____'*m, end='')

def recur(n, m):
    if n == 0:
        tap(m)
        print("\"재귀함수가 뭔가요?\"")
        tap(m)
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        tap(m)
        print("라고 답변하였지.")
    else:
        tap(m)
        print("\"재귀함수가 뭔가요?\"")
        tap(m)
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        tap(m)
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        tap(m)
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recur(n-1, m+1)
        tap(m)
        print("라고 답변하였지.")

recur(int(input()),0)
