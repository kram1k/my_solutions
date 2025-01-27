def main():
    _ = int(input())
    array = [int(x) for x in input().split()]
    k = int(input())
    res = ''
    for _ in range(k):
        start, end = [int(x) - 1 for x in input().split()]
        res += str(str(array[start:end + 1]).count('0')) + '\n'
    return print(res)

if __name__ == '__main__':
    main()