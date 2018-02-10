# 買えるかどうか
def possible_to_purchase(possess, Costs):
    if len(Costs) == 0:
        return False

    # どの商品も買えないなら財宝を売却する
    min_costs = 10**16
    for cost in Costs:
        min_costs = min(cost, min_costs)

    if min_costs > possess:
        return False

    return True

def dfs(possess, Treasures, Costs, Values, point, level):
    print(" " * level, possess, Treasures, Costs, Values, point)
    if possible_to_purchase(possess, Costs):
        # 買えるのなら
        # 買うことのできるすべての商品と売る方法について検討
        for idx, cost in enumerate(Costs):
            if cost <= possess:
                get_point = Values[idx]

                tmp_Costs = Costs[:idx]
                tmp_Values = Values[:idx]

                for idx2 in range(idx+1, len(Costs)):
                    tmp_Costs.append(Costs[idx2])
                    tmp_Values.append(Values[idx2])

                point = max(dfs(
                    possess-cost,
                    Treasures,
                    tmp_Costs,
                    tmp_Values,
                    point+get_point,
                    level+1
                ), point)

    if len(Treasures) == 0:
        return point

    # 売る場合は，停止するすべての商品について検討
    possess += Treasures[0]
    Treasures.pop(0)
    for idx in range(len(Costs)):
        tmp_Costs = Costs[:idx]
        tmp_Values = Values[:idx]

        for idx2 in range(idx+1, len(Costs)):
            tmp_Costs.append(Costs[idx2])
            tmp_Values.append(Values[idx2])

        point = max(dfs(
            possess,
            Treasures,
            tmp_Costs,
            tmp_Values,
            point,
            level+1
        ), point)

    return point




def main():
    global N
    global Treasures
    global Costs
    global Values
    global possess

    N = int(input())

    Treasures = [int(_) for _ in input().split()]
    Costs     = [int(_) for _ in input().split()]
    Values    = [int(_) for _ in input().split()]

    point = dfs(0, Treasures, Costs, Values, 0, 0)

    print(point)




main()
