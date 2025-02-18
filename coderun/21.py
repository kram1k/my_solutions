def main():

    open_abc, open_tag, close_tag,  close_abc = "", [], [], ""
    string = input()
    for char in string:
        if char in ["<", ">"] and len(open_tag) != 2:
            open_tag.append(char)
        elif char in ["<", ">", "/"] and len(open_tag) == 2:
            close_tag.append(char)
        elif char.isalpha() and len(open_tag) != 2:
            open_abc += char
        elif char.isalpha() and len(open_tag) == 2:
            close_abc += char
    print(open_abc, open_tag, close_tag,  close_abc)

if __name__ == "__main__":
    main()
