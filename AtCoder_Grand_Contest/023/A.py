profit_rates = [
-8.04764,
-11.15335,
-0.85312,
-15.16021,
14.21436,
-5.06667,
-1.31180,
0.00000,
-5.02661,
7.39054,
1.86141,
-9.86301,
0.40426,
-8.27354,
5.38944,
3.02822,
3.54711,
10.17407,
28.15389,
1.03950,
15.22634,
67.50000,
41.57783,
-6.09940,
-24.53889,
-1.06270,
4.40387,
-12.86008,
1.29870,
11.77156,
-12.30448,
13.67420,
-0.83682,
6.96203,
33.82643,
-1.62122,
-7.79026,
-15.27214,
-0.57526,
-10.60752,
0.43150,
-1.18153,
-0.76087,
10.51479,
0.29732,
8.49802,
-10.10929,
-1.92503,
3.51240,
6.88623,
16.61998,
-2.88231,
2.96785,
4.88391,
5.57252,
-1.01229,
21.25639,
-14.93976,
-2.33711,
1.30529,
]

def main():
    average = sum(profit_rates) / len(profit_rates)

    deviations = []
    for profit_rate in profit_rates:
        deviations.append(profit_rate - average)

    deviations = list(map(lambda d: d ** 2, deviations))
    var = sum(deviations) / len(deviations)
    sd = var ** 0.5

    print("AVG:{}, VAR:{}, SD:{}".format(average, var, sd))

    sd_1 = 0
    sd_2 = 0
    sd_3 = 0
    for profit_rate in profit_rates:
        if average - sd <= profit_rate <= average + sd:
            sd_1 += 1
        if average - 2 * sd <= profit_rate <= average + 2 * sd:
            sd_2 += 1
        if average - 3 * sd <= profit_rate <= average + 3 * sd:
            sd_3 += 1

    print("μ - σ ～ μ + σ : {}%".format(sd_1 / len(profit_rates)))
    print("μ - 2σ ～ μ + 2σ : {}%".format(sd_2/ len(profit_rates)))
    print("μ - 3σ ～ μ + 3σ : {}%".format(sd_3/ len(profit_rates)))


main()
