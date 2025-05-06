def main():
    n, k = map(int, input().split())
    array = [int(x) for x in input().split()]
    targets = [int(x) for x in input().split()]
    respones = [0 for _ in range(k)]

    for idx, target in enumerate(targets):
        l, r, fl = 0, len(array), False
        m = (l + r) // 2
        while l < r:
            if target < array[m]:
                r = m
                m = (r + l) // 2
            elif target > array[m]:
                l = m + 1
                m = (r + l) // 2
            elif target == array[m]:
                fl = True
                break
        if fl:
            respones[idx] = "YES"
            continue
        respones[idx] = "NO"
    print('\n'.join(respones))


if __name__ == "__main__":
    main()