def main():
    N = int(input()) % 30

    A = ["", "1", "2", "3", "4", "5", "6"]

    for i in range(N):
        A[(i%5)+1], A[(i%5)+2] = A[(i%5)+2], A[(i%5)+1]

    print("".join(A))

main()
