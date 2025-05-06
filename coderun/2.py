def main():
    numbers = set()
    for _ in range(3):
        num = input()
        numbers.add(int(num))
    if len(numbers) < 3:
        return print("NO")
    print("YES")


if __name__ == '__main__':
    main()
