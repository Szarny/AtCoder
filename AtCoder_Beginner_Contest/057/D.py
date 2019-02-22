import sys
import collections

def comb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result



def main():
    N, A, B = [int(_) for _ in sys.stdin.readline().split()]
    V = sorted([int(_) for _ in sys.stdin.readline().split()], reverse=True)
    D = collections.defaultdict(lambda: 0)
    ans = 0

    for v in V:
        D[v] += 1

    for C in range(A, B+1):
        if (sum(V[:C]) / C) == (sum(V[:A]) / A):
            ans += comb(D[V[C-1]], V[:C].count(V[C-1]))

    print((sum(V[:A]) / A))
    print(ans)

main()
