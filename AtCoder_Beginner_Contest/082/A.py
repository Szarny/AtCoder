import math

def main():
    print(
        (lambda nums: math.ceil((nums[0] + nums[1]) / 2))(list(map(int, input().split())))
    )

main()
