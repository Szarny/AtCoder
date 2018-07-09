import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(10000)

# Debug output
def chkprint(*args):
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# --------------------------------------------

dp = None

def main():
    n_station, n_train, src_station, dst_station = [int(_) for _ in input().split()]

    connect = []
    for _ in range(n_station + 1):
        connect.append([])

    trains = {}
    for _ in range(n_train):
        u, v, a, b = [int(_) for _ in input().split()]
        trains[str(u) + str(v)] = {
            "yen": a,
            "snk": b
        }
        connect[u].append(v)
        connect[v].append(u)

    costs_by_exchange_station = [10**20]

    stat_and_cost_arr = [(src_station, 0)]
    costs_yen = {src_station: 0}
    while True:
        new_stat_and_cost_arr = []
        for stat_and_cost in stat_and_cost_arr:
            new_stat_and_cost_arr = []
            current_station, current_cost = stat_and_cost[0], stat_and_cost[1]

            for next_station in connect[current_station]:
                u, v = min(current_station, next_station), max(current_station, next_station)
                if next_station not in costs_yen or current_cost + trains[str(u) + str(v)]["yen"] < costs_yen[next_station]:
                    new_stat_and_cost_arr.append((next_station, current_cost + trains[str(u) + str(v)]["yen"]))
                    costs_yen[next_station] = current_cost + trains[str(u) + str(v)]["yen"]

        if len(new_stat_and_cost_arr) == 0:
            break
        else:
            stat_and_cost_arr = new_stat_and_cost_arr

    for exchange_station in range(1, n_station + 1):
        stat_and_cost_arr = [(exchange_station, costs_yen[exchange_station])]

        costs_snk = {exchange_station: costs_yen[exchange_station]}
        while True:
            new_stat_and_cost_arr = []
            for stat_and_cost in stat_and_cost_arr:
                new_stat_and_cost_arr = []
                current_station, current_cost = stat_and_cost[0], stat_and_cost[1]

                for next_station in connect[current_station]:
                    u, v = min(current_station, next_station), max(current_station, next_station)
                    if next_station not in costs_snk or current_cost + trains[str(u) + str(v)]["snk"] < costs_snk[next_station]:
                        new_stat_and_cost_arr.append((next_station, current_cost + trains[str(u) + str(v)]["snk"]))
                        costs_snk[next_station] = current_cost + trains[str(u) + str(v)]["snk"]

            if len(new_stat_and_cost_arr) == 0:
                break
            else:
                stat_and_cost_arr = new_stat_and_cost_arr

        costs_by_exchange_station.append(costs_snk[dst_station])

    for year in range(n_station):
        print(10**15 - min(costs_by_exchange_station[year+1:]))




main()
