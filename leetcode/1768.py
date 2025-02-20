def mergeAlternately(word1: str, word2: str) -> str:
    len_1 = len(word1)
    len_2 = len(word2)
    res = ""
    top = len_1 if len_2 > len_1 else len_2

    for i in range(top):
        res += word1[i]
        res += word2[i]

    if len_1 > len_2:
        res += word1[top:]
    else:
        res += word2[top:]
    return res


print(mergeAlternately("abc", "pqr"))
