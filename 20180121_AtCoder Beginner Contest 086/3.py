def main():
  N = int(input())

  moves = []

  for i in range(N):
    moves.append([int(j) for j in input().split()])

  # 移動前
  pre_t = 0
  pre_x = 0
  pre_y = 0

  for move in moves:
    new_t, new_x, new_y = move[0], move[1], move[2]

    # 時刻の差分
    delta_t = new_t - pre_t

    # 位置の差分
    delta_x = abs(new_x - pre_x)
    delta_y = abs(new_y - pre_y)
    delta_sum = delta_x + delta_y

    remain_time = delta_t - delta_sum

    # 移動量と時間が一致
    if remain_time == 0:
      pre_t, pre_x, pre_y = new_t, new_x, new_y

    # 移動量の方が少ない
    elif remain_time > 0:
      # 残り時間が偶数なら行ったり来たりでOK
      if remain_time % 2 == 0:
        pre_t, pre_x, pre_y = new_t, new_x, new_y
      else:
        print("No")
        return

    # 時間が足りない
    else:
      print("No")
      return

  print("Yes")
  return

main()
