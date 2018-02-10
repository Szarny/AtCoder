def main():
    S = list(input())

    B = "aiueo"
    for b in B:
        while b in S:
            S.remove(b)

    R = ""
    for l in S:
        R += l
    print(R)

main()
