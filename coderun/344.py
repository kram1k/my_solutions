def main():

    N, M = [int(x) for x in input().split()]
    white = int(input())
    white_pos = [[int(x) for x in input().split()] for _ in range(white)]
    black = int(input())
    black_pos = [[int(x) for x in input().split()] for _ in range(black)]
    move = input()
    is_white = 1 if move == 'white' else 0
    directions = [
        [-1, -1],  # top left
        [-1, 1],   # top right
        [1, -1],   # bottom left
        [1, 1]     # bottom right
    ]

    def is_opponent_found(
        target_x: int,
        target_y: int,
        pos: list[list[int]]
    ) -> bool:
        for i in pos:
            if i[0] == target_x and i[1] == target_y:
                return True
        return False

    def is_empty_blocker(
        black_pos: list[list[int]],
        white_pos: list[list[int]],
        blocker_x: int,
        blocker_y: int
    ) -> bool:
        for i in black_pos:
            if i[0] == blocker_x and i[1] == blocker_y:
                return False
        for j in white_pos:
            if j[0] == blocker_x and j[1] == blocker_y:
                return False
        return True

    if is_white:
        for i in range(white):
            x, y = white_pos[i]
            for j in range(4):
                target_x = x + directions[j][0]
                target_y = y + directions[j][1]
                blocker_x = x + 2 * directions[j][0]
                blocker_y = y + 2 * directions[j][1]
                if (1 <= target_x <= N
                    and 1 <= target_y <= M
                    and 1 <= blocker_x <= N
                    and 1 <= blocker_y <= M):
                        if is_opponent_found(target_x, target_y, black_pos):
                            if is_empty_blocker(black_pos, white_pos, blocker_x, blocker_y):
                                print("Yes")
                                return
    else:
        for i in range(black):
            x, y = black_pos[i]
            for j in range(4):
                target_x = x + directions[j][0]
                target_y = y + directions[j][1]
                blocker_x = x + 2 * directions[j][0]
                blocker_y = y + 2 * directions[j][1]
                if (1 <= target_x <= N
                    and 1 <= target_y <= M
                    and 1 <= blocker_x <= N
                    and 1 <= blocker_y <= M):
                        if is_opponent_found(target_x, target_y, white_pos):
                            if is_empty_blocker(black_pos, white_pos, blocker_x, blocker_y):
                                print("Yes")
                                return
    print("No")


if __name__ == '__main__':
    main()
