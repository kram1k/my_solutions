def main():
    n, m, k = [int(x) for x in input().split()]
    matrix = [0 for _ in range(n)]
    
    for i in range(n):
        matrix[i] = [int(x) for x in input().split()]
    
    result = ''
    for _ in range(k):
        mx_sum = 0
        x_1, y_1, x_2, y_2 = [int(x )- 1 for x in input().split()]
        mx_sum += sum(matrix[x_1][y_1:]) + sum(matrix[x_2][y_1:])
        result += str(mx_sum) + '\n'
    return print(result)
    

if __name__ == '__main__':
    main()