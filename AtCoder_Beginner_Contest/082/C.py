from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    D = defaultdict(lambda: 0)

    for a in A:
        D[a] += 1

    r = 0
    for k,v in D.items():
        if k < v:
            r += v - k
        elif k > v:
            r += v

    print(r)

main()
