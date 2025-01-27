from decimal import Decimal, getcontext
getcontext().prec = 12


def main():
    n = int(input())
    servers = []
    for _ in range(n):
        a, b = map(int, input().split())
        servers.append((a, b))
    
    error_probabilities = []
    for i in range(n):
        error_probabilities.append((servers[i][0] / 100) * (servers[i][1] / 100) / sum((s[0] / 100) * (s[1] / 100) for s in servers))
    
    for p in error_probabilities:
        print("{:.12f}".format(p))


if __name__ == '__main__':
    main()