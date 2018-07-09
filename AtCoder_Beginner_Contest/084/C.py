def main():
    N = int(input())

    times, start, interval = [], [], []
    for i in range(N-1):
        t, s, i = list(map(int, input().split()))
        times.append(t)
        start.append(s)
        interval.append(i)

    for src_station_idx in range(N-1):
        current_total_time = start[src_station_idx] + times[src_station_idx]

        for via_station_idx in range(src_station_idx+1, N-1):
            moving_time = times[via_station_idx]

            # 次に来る電車までの待ち時間を計測する
            if current_total_time <= start[via_station_idx]:
                waiting_time = start[via_station_idx] - current_total_time
            else:
                passed_time_from_start = current_total_time - start[via_station_idx]
                passed_time_from_before = passed_time_from_start % interval[via_station_idx]

                if passed_time_from_before == 0:
                    waiting_time = 0
                else:
                    waiting_time = interval[via_station_idx] - passed_time_from_before

            current_total_time += waiting_time + moving_time

        print(current_total_time)

    print(0)

main()
