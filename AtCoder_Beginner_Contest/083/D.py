def main():
    S = input()
    N = len(S)

    minimum_t = 100000000
    pre_letter = S[0]

    for idx in range(1, N):
        if S[idx] != pre_letter:
            minimum_t = min(max(idx, N-idx), minimum_t)
            pre_letter = S[idx]
        else:
            continue

    if minimum_t == 100000000:
        print(N)
    else:
        print(minimum_t)

main()
