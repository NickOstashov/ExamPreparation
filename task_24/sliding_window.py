"""
Задача: дан массив чисел,
нужно найти попоследовательность из 3-х чисел с максимальной суммой
"""
import random

def solution():
    # Генерация случайной длины массива от 1000 до 100_000
    length = random.randint(1000, 100_000)

    # Генерация массива с произвольными числами от -5 до 5
    random_array = [random.randint(-5, 5) for _ in range(length)]

    arr = [2, 1, 4, 5, -10, 1]

    max_sum = -1
    for i in range(len(arr) - 2):
        l_sum = sum(arr[i: i + 3])

        if l_sum > max_sum:
            max_sum = l_sum

    return max_sum


def main():
    print(solution())

if __name__ == "__main__":
    main()