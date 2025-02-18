def update_lst(array: list[int], idx: str, new_val: int) -> list[int]:
    array[int(idx) - 1] += int(new_val)
    return array


def back_old_value(
    array: list[int],
    idx: str, old_array: list[int]
) -> list[int]:
    array[int(idx) - 1] = old_array[int(idx) - 1]
    return array


def sum_two_arrays(arr_1: list[int], arr_2: list[int], lenght) -> int:
    counter = 0
    for i in range(lenght):
        if arr_1[i] > arr_2[i]:
            counter += arr_1[i]
        else:
            counter += arr_2[i]
    return counter


def main():
    n = int(input())
    a, b, const_a, const_b = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]
    char_a, char_b = input().split(), input().split()
    for idx in range(n):
        a[idx] = int(char_a[idx])
        b[idx] = int(char_b[idx])
        const_a[idx] = int(char_a[idx])
        const_b[idx] = int(char_b[idx])
    m = int(input())
    res = [0 for _ in range(m)]
    sertificats = [[x for x in input().split()] for _ in range(m)]

    for j in range(m):
        string = sertificats[j]
        index, tip, d = string
        if j >= 2:
            if sertificats[j - 2][1] == "1":
                a = back_old_value(a, sertificats[j - 2][0], const_a)
                if tip == "1":
                    a = update_lst(a, index, d)
                    res[j] = sum_two_arrays(a, b, n)
                else:
                    b = update_lst(b, index, d)
                    res[j] = sum_two_arrays(a, b, n)
            else:
                b = back_old_value(b, sertificats[j - 2][0], const_b)
                if tip == "1":
                    a = update_lst(a, index, d)
                    res[j] = sum_two_arrays(a, b, n)
                else:
                    b = update_lst(b, index, d)
                    res[j] = sum_two_arrays(a, b, n)
        else:
            if tip == "1":
                res[j] = sum_two_arrays(a, b, n)
                a = update_lst(a, index, d)
            else:
                res[j] = sum_two_arrays(a, b, n)
                b = update_lst(b, index, d)
    print(*res)


if __name__ == "__main__":
    main()
