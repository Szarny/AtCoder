def main():
    a, b, c, d = list(map(int, input().split()))

    l = a + b
    r = c + d

    if l > r:
        print("Left")
    elif l < r:
        print("Right")
    else:
        print("Balanced")

main()
