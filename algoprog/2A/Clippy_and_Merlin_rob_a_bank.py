def main():
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    
    idx_max_value = array.index(max(array))
    array[idx_max_value] = 0
    for _ in range(n - 1):
        idx_second_max_value = array.index(max(array))
        lenght = array[idx_max_value:idx_second_max_value]
        if lenght < k + 1:
            array[idx_second_max_value] = 0
        else:
            print(f'{idx_max_value} {idx_second_max_value}')
        
    
    
if __name__ == '__main__':
    main()