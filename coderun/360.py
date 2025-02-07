def main():
    n = int(input())
    arr = sorted([int(x) for x in input().split()])
    db: dict[int, int] = {}
    for i in arr:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1

    mx_db_val = max(db.values())
    q = 0
    for k, v in db.items():
        if v == mx_db_val:
            if k > q:
                q = k
    print(q)


if __name__ == "__main__":
    main()