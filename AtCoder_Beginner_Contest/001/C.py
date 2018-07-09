import math
def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x)))/p

def main():
    deg, dis = [int(_) for _ in input().split()]

    result_deg = ""
    deg *= 10
    if 1125 <= deg < 3375:
        result_deg = "NNE"
    elif deg < 5625:
        result_deg = "NE"
    elif deg < 7875:
        result_deg = "ENE"
    elif deg < 10125:
        result_deg = "E"
    elif deg < 12375:
        result_deg = "ESE"
    elif deg < 14625:
        result_deg = "SE"
    elif deg < 16875:
        result_deg = "SSE"
    elif deg < 19125:
        result_deg = "S"
    elif deg < 21375:
        result_deg = "SSW"
    elif deg < 23625:
        result_deg = "SW"
    elif deg < 25875:
        result_deg = "WSW"
    elif deg < 28125:
        result_deg = "W"
    elif deg < 30375:
        result_deg = "WNW"
    elif deg < 32625:
        result_deg = "NW"
    elif deg < 34875:
        result_deg = "NNW"
    else:
        result_deg = "N"

    if dis < 0.2*60+3:
        result_deg = "C"
        result_dis = 0
    elif dis < 1.5*60+3:
        result_dis = 1
    elif dis < 3.3*60+3:
        result_dis = 2
    elif dis < 5.4*60+3:
        result_dis = 3
    elif dis < 7.9*60+3:
        result_dis = 4
    elif dis < 10.7*60+3:
        result_dis = 5
    elif dis < 13.8*60+3:
        result_dis = 6
    elif dis < 17.1*60+3:
        result_dis = 7
    elif dis < 20.7*60+3:
        result_dis = 8
    elif dis < 24.4*60+3:
        result_dis = 9
    elif dis < 28.4*60+3:
        result_dis = 10
    elif dis < 32.6*60+3:
        result_dis = 11
    else:
        result_dis = 12

    print(result_deg, result_dis)

main()
