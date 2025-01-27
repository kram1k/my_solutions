def main():
    n, m = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    
    result = ''
    for _ in range(m):
        left, right = [int(x) for x in input().split()]
        result += str(sum(array[left - 1:right])) + '\n'
    return print(result)


if __name__ == '__main__':
    main()