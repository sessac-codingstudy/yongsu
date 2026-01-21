#https://www.acmicpc.net/problem/25501

#재귀함수 기초

import sys
def input():
    return sys.stdin.readline().rstrip()

def recursion(s, l, r, n):
    if l >= r: return 1, n
    elif s[l] != s[r]: return 0, n
    else: return recursion(s, l+1, r-1, n+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for _ in range(int(input())):
    text = input()
    result = isPalindrome(text)
    print(result[0], result[1])
