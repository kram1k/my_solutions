def reverseVowels(s: str):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    lst_vowels = []
    for char in s:
        if char in vowels:
            lst_vowels.append(char)
    res = ""
    j = 0
    lst_vowels.reverse()
    for i in range(len(s)):
        if s[i] in vowels:
            res += lst_vowels[j]
            j += 1
        else:
            res += s[i]
    return res


print(reverseVowels("IceCreAm"))