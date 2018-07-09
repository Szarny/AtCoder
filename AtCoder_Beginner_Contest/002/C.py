def main():
    xa, ya, xb, yb, xc, yc = [int(_) for _ in input().split()]

    xb -= xa
    yb -= ya
    xc -= xa
    yc -= ya

    print(abs(xb*yc - yb*xc) / 2)

main()
