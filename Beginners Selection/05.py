import sys

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    ans = 0

    for nA in range(A + 1):
        for nB in range(B + 1):
            for nC in range(C + 1):
                if nA * 500 + nB * 100 + nC * 50 == X:
                    ans += 1

    print(ans)

main()
