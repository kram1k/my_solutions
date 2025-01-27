def main():
    def elem_int(s, x):
        return 1 if x in s else 0
    
    def jewelery_count(j, s):
        return sum(elem_int(j, x) for x in s)
    j = input()
    s = input()
    print(jewelery_count(j, s))


if __name__ == '__main__':
    main()