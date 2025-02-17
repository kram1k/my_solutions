def main():
    string = [x for x in input().split()]
    days = int(string[0])
    day = string[1]
    month: list[list[str]] = []

    if day == "Monday":
        month.append([])
    elif day == "Tuesday":
        month.append([".." for _ in range(1)])
    elif day == "Wednesday":
        month.append([".." for _ in range(2)])
    elif day == "Thursday":
        month.append([".." for _ in range(3)])
    elif day == "Friday":
        month.append([".." for _ in range(4)])
    elif day == "Saturday":
        month.append([".." for _ in range(5)])
    else:
        month.append([".." for _ in range(6)])
    week_count = 0

    for i in range(1, days + 1):
        if len(month[week_count]) < 7:
            if i < 10:
                month[week_count].append(f".{i}")
            else:
                month[week_count].append(f"{i}")
        else:
            month.append([])
            week_count += 1
            if i < 10:
                month[week_count].append(f".{i}")
            else:
                month[week_count].append(f"{i}")
    for q in month:
        print(*q)


if __name__ == "__main__":
    main()
