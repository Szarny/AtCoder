def main():
    print((lambda x: x[1]//x[0])(list(map(int, input().split()))))

main()
