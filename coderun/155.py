def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique_count = 0
    element_count = {}
    
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    for count in element_count.values():
        if count == 1:
            unique_count += 1
    
    return print(unique_count)

    
if __name__ == '__main__':
    main()