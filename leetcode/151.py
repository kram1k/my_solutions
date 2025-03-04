def reverseWords(s: str) -> str:
    array = s.strip(" ").split(" ")
    array.reverse()
    array = [x for x in array if x != ""]
    res = ''
    for idx, i in enumerate(array):
        if idx != len(array) - 1:
            res += i + " "
        else:
            res += i
    return res

print(reverseWords("a good   example"))
