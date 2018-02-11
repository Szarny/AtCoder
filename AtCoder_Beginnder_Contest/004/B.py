def main():
    c = []

    for _ in range(4):
        c.append(input().split())

    c_new = []

    for i in range(3, -1, -1):
        c_new.append([])
        for j in range(3, -1, -1):
            c_new[3-i].append(c[i][j])

    for i in range(4):
        for j in range(4):
            if j != 3:
                print(c_new[i][j], end=" ")
            else:
                print(c_new[i][j])

main()
