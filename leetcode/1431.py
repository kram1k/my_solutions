
def kidsWithCandies(candies: list[int], extraCandies: int):
    bool_arr = [0 for _ in range(len(candies))]
    for idx, x in enumerate(candies):
        old_x = x
        candies[idx] += extraCandies
        if candies[idx] == max(candies):
            bool_arr[idx] = True
        else:
            bool_arr[idx] = False
        candies[idx] = old_x
    return bool_arr


print(kidsWithCandies([12,1,12], 10))