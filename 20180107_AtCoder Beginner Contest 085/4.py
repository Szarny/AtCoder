import math

def main():
    N, H = map(int, input().split())

    cuts = []
    throws = []
    for i in range(N):
        tmp = [int(j) for j in input().split()]
        cuts.append(tmp[0])
        throws.append(tmp[1])

    max_cut = max(cuts)
    t1 = 0

    throws.sort(reverse=True)

    for throw in throws:
        if throw < max_cut:
            break
        H -= throw
        t1 += 1

    t2 = math.ceil(H / max_cut)

    print(t1 + t2)




main()
