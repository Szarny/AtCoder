def main():
    Row, Col = list(map(int, input().split()))

    y_src, x_src = list(map(int, input().split()))
    y_src -= 1
    x_src -= 1
    y_dst, x_dst = list(map(int, input().split()))
    y_dst -= 1
    x_dst -= 1

    board = []
    for r in range(Row):
        board.append(list(input()))

    queue = [[y_src, x_src]]

    n_move = 0
    delta_x = [-1, 0, 0, 1]
    delta_y = [0, -1, 1, 0]

    while len(queue) != 0:
        next_queue = []

        for item in queue:
            if item[0] == y_dst and item[1] == x_dst:
                print(n_move)
                return

            board[item[0]][item[1]] = n_move

            for dx, dy in zip(delta_x, delta_y):
                if (0 <= item[0]+dy < Row)  and \
                    (0 <= item[1]+dx < Col) and \
                    (board[item[0]+dy][item[1]+dx] == ".") and \
                    ([item[0]+dy, item[1]+dx] not in next_queue):
                    next_queue.append([item[0]+dy, item[1]+dx])

        queue = next_queue
        n_move += 1

main()
