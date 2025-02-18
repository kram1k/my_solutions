from collections import defaultdict


def main():
    n = int(input())
    names = [0 for _ in range(n)]
    for x in range(n):
        names[x] = input()

    db = defaultdict(int)
    for name in names:
        db[name] += 0

    m = int(input())
    left_old = 0
    right_old = 0
    for _ in range(m):
        arr_string = input().split(sep=" ")
        command, player = arr_string[0], arr_string[1]
        left_command, right_command = [int(x) for x in command.split(":")]
        left_goal = left_command - left_old
        right_goal = right_command - right_old
        left_old, right_old = left_command, right_command
        db[player] += left_goal
        db[player] += right_goal

    max_score = max(db.values())
    top_scorers = [player for player, score in db.items() if score == max_score]
    print(f"{sorted(top_scorers)[-1]} {max_score}")


if __name__ == "__main__":
    main()