#https://school.programmers.co.kr/learn/courses/30/lessons/12907

#DP문제
#A코드는 직접 작성한 재귀풀이법(시간초과로 오답)
#B코드는 용재형님의 DP풀이법

# A
import sys
sys.setrecursionlimit(10**7)

def solution(n, money):
    money.sort()
    count = [0]
    def recur(num, li):
        if len(li) == 0:
            return
        x = li[-1]
        for i in range(0, num//x+1):
            left = num - i*x
            if left == 0:
                count[0] += 1
                return
            recur(left, li[0:-1])
        return
    recur(n, money)
    return count[0] % 1_000_000_007

# B
def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in money:
        for x in range(coin, n+1):
            dp[x] = (dp[x] + dp[x-coin]) % MOD
    
    return dp[n]
