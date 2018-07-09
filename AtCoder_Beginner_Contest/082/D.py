import sys
sys.setrecursionlimit(50000)

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x_dst = None
y_dst = None

def dfs(x, y, d, S):

    if len(S) == 0:
        if x == x_dst and y == y_dst:
            print("Yes")
            sys.exit()
        else:
            return

    if S[0] == "F":
        dfs(x+dx[d], y+dy[d], d, S[1:])
    else:
        dfs(x, y, (d-1)%4, S[1:])
        dfs(x, y, (d+1)%4, S[1:])

def main():
    global x_dst
    global y_dst

    S = input()
    x_dst, y_dst = list(map(int, input().split()))

    x, y = 0, 0
    d = RIGHT

    dfs(x, y, d, S)

    print("No")

main()
