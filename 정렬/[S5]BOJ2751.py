import sys
def input():
    return sys.stdin.readline().rstrip()

def sorter(length):
    sorter = []
    for _ in range(length):
        sorter.append(int(input()))
    sorter.sort()
    for i in sorter:
        print(i)

sorter(int(input()))
