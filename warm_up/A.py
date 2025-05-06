def main():
    n = int(input())
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    elif n == 2:
        print(4)
    else:
        a, b, c = 1, 2, 4
        for _ in range(3, n + 1):
            next_val = c + b + a
            a, b, c = b, c, next_val
        print(c)


if __name__ == "__main__":
    main()
