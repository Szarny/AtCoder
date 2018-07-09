N = int(input())

Board = []
for i in range(2):
  Board.append(list(map(int, input().split())))

max_candies = 0
for gotodown_index in range(N):

  upper_candies = sum(Board[0][:gotodown_index+1])
  lower_candies = sum(Board[1][gotodown_index:])
  candies = upper_candies + lower_candies

  if candies > max_candies:
    max_candies = candies

print(max_candies)
