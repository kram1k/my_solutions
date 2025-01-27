def main():
    input_lenght = int(input())
    tests = [0 for _ in range(input_lenght * 2)]

    for idx, _ in enumerate(tests):
        query = input()
        if query.isdigit():
            tests[idx] = int(query)
        else:
            tests[idx] = sorted([int(x) for x in query.split()])

    result = ''
    array: list[int] = []
    for val in tests:
        if type(val) is int:
            array = [0 for _ in range(val - 1)]
        else:
            x = 0
            while x < len(array):
                array[x] = val[x] ^ val[x + 1]
                x += 1
            result += str(min(array)) + '\n'
            array.clear()
    print(result)


if __name__ == '__main__':
    main()