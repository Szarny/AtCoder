import math

a, b = map(int, input().split())

result = int(str(a) + str(b))

result2 = math.floor(math.sqrt(result))

if result2 ** 2 == result:
  print("Yes")
else:
  print("No")
