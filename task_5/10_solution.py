#https://inf-ege.sdamgia.ru/problem?id=7663
def solution_7663():
    def merge_vals(num_1: int, num_2: int) -> int:
        array = [num_1, num_2]
        array.sort(reverse=True)
        merge_str = ''
        for item in array:
            merge_str += str(item)

        return int(merge_str)

    def calc_new_val(n: int) -> int:
        n_str = str(n)
        num_1 = int(n_str[0]) + int(n_str[1])
        num_2 = int(n_str[1]) + int(n_str[2])

        return merge_vals(num_1, num_2)

    n, r = 100, 0
    while r != 1412:
        n += 1
        r = calc_new_val(n)

    print(n)


def main():
    solution_7663()


if __name__ == '__main__':
    main()