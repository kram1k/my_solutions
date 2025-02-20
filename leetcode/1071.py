from math import gcd


def gcdOfStrings(str1: str, str2: str):
    if len(str1) < len(str2):
        return gcdOfStrings(str2, str1)
    if len(str2) == 0:
        return str1
    if len(str1) > len(str2):
        return str1[:gcd(len(str1), len(str2))]


print(gcdOfStrings("ABCABC", "ABC"))