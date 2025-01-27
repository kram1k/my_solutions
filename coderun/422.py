from math import ceil

def main():
    A, B, N = int(input()), int(input()), int(input())
    if A > B:
        print("Yes")
    else:
        minB = ceil(B / N)
        print("Yes" if A > minB else "No")


if __name__ == '__main__':
    main()