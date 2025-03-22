"""
Задача: дан массив чисел,
нужно найти попоследовательность из 3-х чисел с максимальной суммой
"""
import random
import sys

def solution():
    arr = [2, 1, -10, 11, -1, 3, 2]

    max_sum = -sys.maxsize
    for i in range(len(arr) - 2):
        l_sum = sum(arr[i: i + 3])

        if l_sum > max_sum:
            max_sum = l_sum

    print(max_sum)


def main():
    solution()


if __name__ == "__main__":
    main()