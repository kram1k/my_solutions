import math


def main():
    x, y = map(int, input().split())
    if y % x:
        return print("0")
    y //= x
    count = 0
    for i in range(1, int(math.sqrt(y)) + 1):
        if y % i == 0 and math.gcd(i, y // i) == 1:
            count += 1 + (i * i != y)

    return print(count)


if __name__ == '__main__':
    main()