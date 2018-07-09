# だめです
# 何がダメかはわかっている

def main():
  N_PEOPLE, N_INFO = list(map(int, input().split()))

  info_list = []
  for i in range(N_INFO):
    l, r, d = list(map(int, input().split()))
    info_list.append({
      "left":  l-1,
      "right": r-1,
      "dist":  d
    })

  # 各人の位置(不定の場合はNone)
  locations = [None] * N_PEOPLE

  # 各人が登場したか
  appeared = []

  if len(info_list) == 0:
    print("Yes")
    return

  for info in info_list:
    # 左右の人物が共に初登場なら，とりあえずleftを0において，rightを距離の分だけ離す
    if info["left"] not in appeared and info["right"] not in appeared:
      locations[info["left"]] = 0
      locations[info["right"]] = info["dist"]

      appeared.append(info["left"])
      appeared.append(info["right"])

      continue

    # 左の人物だけが初登場なら，rightの人物の位置から見てdist分左におく
    if info["left"] not in appeared and info["right"] in appeared:
      locations[info["left"]] = locations[info["right"]] - info["dist"]

      appeared.append(info["left"])

      continue


    # 右の人物だけが初登場なら，leftの人物から見てdist分右におく
    if info["left"] in appeared and info["right"] not in appeared:
      locations[info["right"]] = locations[info["left"]] + info["dist"]

      appeared.append(info["right"])

      continue

    # 両方の人物が既出なら，距離が正しいかチェックする
    # 正しくなければアウト
    if info["left"] in appeared and info["right"] in appeared:
      if locations[info["right"]] - locations[info["left"]] != info["dist"]:
        print("No")
        return

  print("Yes")

main()
