import sys

def main():
    N = int(input())
    A = [int(_) for _ in input().split()]

    t = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                print(t)
                sys.exit()
        t += 1

main()
