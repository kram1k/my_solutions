def main():
    o, c = [int(x) for x in input().split()]
    offers = sorted([int(x) for x in input().split()])
    customers = sorted([int(x) for x in input().split()], reverse=True)
    res = 0
    for i in range(min(o, c)):
        if customers[i] > offers[i]:
            res += customers[i] - offers[i]
        else:
            break
    print(res)


if __name__ == '__main__':
    main()
