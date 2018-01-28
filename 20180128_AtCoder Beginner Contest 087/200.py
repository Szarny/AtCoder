n_five_hundred_coin = int(input())
n_hundred_coin = int(input())
n_fifty_coin = int(input())
total_money = int(input())

n_pattern = 0
for five_hundred_coin in range(n_five_hundred_coin+1):
  # この時点で合計を超えていればアウト
  if five_hundred_coin * 500 > total_money:
    break

  for hundred_coin in range(n_hundred_coin+1):
    # この時点で合計を超えていればアウト
    if five_hundred_coin * 500 + hundred_coin * 100 > total_money:
      break

    remain_money = total_money - five_hundred_coin * 500 - hundred_coin * 100
    need_fifty_coin = remain_money / 50

    if need_fifty_coin <= n_fifty_coin:
      n_pattern += 1

print(n_pattern)
