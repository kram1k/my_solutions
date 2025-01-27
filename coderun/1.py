
def main(arr: list) -> int:
    result: list = sorted(arr)
    return result[1]
        

if __name__ == '__main__':
    print(main([int(i) for i in input().split()]))