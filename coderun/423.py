import sys
from bisect import bisect_left

def find_nearest_bus_stop(bus_stops, cord):
    pos = bisect_left(bus_stops, cord)
    if pos == 0:
        return 1
    if pos == len(bus_stops):
        return len(bus_stops)
    before = bus_stops[pos - 1]
    after = bus_stops[pos]
    if after - cord < cord - before:
        return pos + 1
    else:
        return pos

def main():
    count_cord, count_bus = [int(x) for x in input().split()]
    bus_stops = [int(x) for x in input().split()]
    cords = [int(x) for x in input().split()]

    for cord in cords:
        res = find_nearest_bus_stop(bus_stops, cord)
        print(res)

if __name__ == '__main__':
    main()