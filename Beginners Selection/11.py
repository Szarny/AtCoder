import sys

def main():
    N = int(input())
    t, x, y = 0, 0, 0

    for _ in range(N):
        next_t, next_x, next_y = [int(__) for __ in input().split()]

        delta_t = next_t - t
        distance = abs(next_x - x) + abs(next_y - y)

        if distance > delta_t:
            print("No")
            sys.exit()

        if (delta_t - distance) % 2 != 0:
            print("No")
            sys.exit()

        t, x, y = next_t, next_x, next_y

    print("Yes")

main()
