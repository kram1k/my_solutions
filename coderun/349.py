import json


def main():
    n, m = [int(x) for x in input().split()]
    all_offers: dict[str: list]= {}
    all_offers["offers"] = []
    for i in range(n):
        feed = json.loads(input())
        all_offers['offers'] += feed['offers']
    all_offers['offers'] = all_offers['offers'][:m]
    print(json.dumps(all_offers, indent=4))


if __name__ == "__main__":
    main()
