N = None
R = None
dp = None

def is_clique(binary):
    group = []
    for i, b in enumerate(binary):
        if b == "1":
            group.append(i)
    for i,p in enumerate(group):
        for j,q in enumerate(group):
            if i == j:
                continue

            if not R[p][q]:
                return False

    return True


def main():
    global N
    global R

    N, M = [int(_) for _ in input().split()]

    R = []
    for _ in range(N):
        R.append([])
        for __ in range(N):
            R[_].append(False)

    for _ in range(M):
        i, j = [int(__) for __ in input().split()]
        R[i-1][j-1] = True
        R[j-1][i-1] = True

    max_clique = 1

    for k in range(1, 2**N):
        binary = bin(k)[2:]

        if len(binary) != N:
            short = N - len(binary)
            binary = "0"*short + binary

        if is_clique(binary):
            max_clique = max(len(binary.replace("0", "")), max_clique)

    print(max_clique)


main()
