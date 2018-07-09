"""
N = 50

Q
1   50
4
"""

def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append([int(__) for __ in input().split()])

    Q = int(input())
    limit = []
    for _ in range(Q):
        limit.append(int(input()))



main()
