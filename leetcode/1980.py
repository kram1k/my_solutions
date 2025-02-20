from random import choice


def findDifferentBinaryString(nums):
    l = len(nums)
    array_integers = [0 for _ in range(l)]

    for idx, binar in enumerate(nums):
        array_integers[idx] = int(binar, 2)

    for _ in range(100):
        s = ""
        for x in range(l):
            s += choice(["0", "1"])
        if s not in nums:
            return s


print(findDifferentBinaryString(["01","10"]))
