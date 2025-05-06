def main():
    s = input()
    long_lst = []
    if len(s) == 1:
        long_lst.append(s)
    else:
        for idx, char in enumerate(s[:-1]):
            if s[idx + 1].isdigit():
                long_lst.append(f"{s[idx] * int(s[idx + 1])}")
            elif s[idx].isdigit():
                continue
            else:
                long_lst.append(char)
    print("".join(long_lst))


if __name__ == "__main__":
    main()