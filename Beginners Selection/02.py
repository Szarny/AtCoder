def main():
    a, b = [int(_) for _ in input().split()]
    print("Even") if a * b % 2 == 0 else print("Odd")

main()
