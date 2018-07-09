def main():
    S1 = input()
    S2 = input()

    for s1, s2 in zip(S1, S2):
        if s1 == s2 or (s1 == "@" and s2 == "@"):
            continue

        elif s1 == "@":
            if s2 not in "atcoder":
                print("You will lose")
                return

        elif s2 == "@":
            if s1 not in "atcoder":
                print("You will lose")
                return



        elif s1 != s2:
            print("You will lose")
            return

    print("You can win")



main()
