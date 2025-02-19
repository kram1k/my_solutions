def main():
    n = int(input())
    tasks = []
    for _ in range(n):
        d, w = map(int, input().split())
        tasks.append((d, w))

    tasks.sort(key=lambda x: x[1], reverse=True)

    schedule = [0] * (n + 1)
    total_stress = 0

    for task in tasks:
        deadline, stress = task

        placed = False
        for i in range(min(deadline, n), 0, -1):
            if schedule[i] == 0:
                schedule[i] = 1
                placed = True
                break

        if not placed:
            total_stress += stress

    print(total_stress)


if __name__ == '__main__':
    main()