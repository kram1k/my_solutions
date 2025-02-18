def main():
    n = int(input())
    divisor_count = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_count[j] += 1

    max_divisors = 0
    number_with_max_divisors = 0

    for i in range(1, n + 1):
        if divisor_count[i] >= max_divisors:
            max_divisors = divisor_count[i]
            number_with_max_divisors = i
    print(number_with_max_divisors)
    print(max_divisors)


if __name__ == "__main__":
    main()
