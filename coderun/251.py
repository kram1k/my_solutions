
def main():
    string = input()
    string_2 = input()
    uni_string = set(string_2)
    res = []
    counter = 0
    for i in string:
        if i in uni_string:
            counter += 1
            uni_string.remove(i)
        elif i not in uni_string and len(uni_string) != 0 and counter != 0:
            counter += 1
        if len(uni_string) == 0:
            res.append(counter)
            uni_string = set(string_2)
            counter = 0
    # if 
    print(min(res)) if len(res) != 0 else print(0)

if __name__ == '__main__':
    main()
