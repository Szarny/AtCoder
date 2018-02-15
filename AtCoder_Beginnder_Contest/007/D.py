def solve_all(begin, end):
    pass

def solve_part(begin, end):
    n_forbidden = 0

    for number in range(begin, end+1):
        numstr = str(number)
        if ("4" in numstr) or ("9" in numstr):
            n_forbidden += 1

    print(n_forbidden)

def main():
    begin, end = list(map(int, input().split()))

    solve_part(begin, end)

main()
