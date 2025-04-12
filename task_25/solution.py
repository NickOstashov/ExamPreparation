import math

class Util:
    @staticmethod
    def output(lst: list[tuple], rev : bool = False) -> None:
        if not rev:
            for item in lst:
                print(item[0], item[1])
        else:
            for i in range(len(lst) - 1, -1, -1):
                print(lst[i][0], lst[i][1])

    @staticmethod
    def generate_sequence(mask: str, max_value: int) -> list[int]:
        """
        Генерирует все числа <= max_value, соответствующие маске.

        :param mask: Маска (например, "12*4?5").
        :param max_value: Максимально допустимое число.
        :return: Отсортированный список подходящих чисел.
        """
        if not mask:
            return []

        numbers = []

        def backtrack(current: str, remaining_mask: str):
            if not remaining_mask:
                if current:
                    num = int(current)
                    if num <= max_value:
                        numbers.append(num)
                return

            char = remaining_mask[0]
            remaining = remaining_mask[1:]

            if char == '*':
                # Вариант 1: пропускаем '*' (пустая последовательность)
                backtrack(current, remaining)

                # Вариант 2: добавляем цифры (но не превышаем max_value)
                for digit in '0123456789':
                    new_current = current + digit
                    if new_current and int(new_current) > max_value:
                        continue
                    backtrack(new_current, '*' + remaining)

            elif char == '?':
                for digit in '0123456789':
                    new_current = current + digit
                    if new_current and int(new_current) > max_value:
                        continue
                    backtrack(new_current, remaining)

            else:  # обычная цифра
                new_current = current + char
                if new_current and int(new_current) > max_value:
                    return
                backtrack(new_current, remaining)

        backtrack("", mask)
        return sorted(list(set(numbers)))

    @staticmethod
    def get_divs(n : int) -> list[int]:
        res = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                res.append(i)
                res.append(n//i)

        return sorted(set(res))

    @staticmethod
    def is_two_pow(n : int) -> bool:
        """определяет: является ли число 'n' степенью числа 2"""
        if n <= 0:
            return False

        log = math.log2(n)
        return log.is_integer()


class Solution:
    @staticmethod
    def run_45259() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=45259"""
        res = list()
        for i in range (123450708, 123459798):
            div = i // 23
            if (i % 10 == 8) and ((i//100)% 10 == 7) and (i % 23 == 0):
                res.append((i, div))

        Util.output(res)

    @staticmethod
    def run_47229() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=47229"""
        seq = Util.generate_sequence(mask="1?2139*4", max_value=10**10)
        res = list()
        for i in seq:
            div = i // 2023
            if i % 2023 == 0:
                res.append((i, div))

        Util.output(res)

    @staticmethod
    def run_63074() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=63074"""
        for i in range(0, (10**10 + 1) ,3147):
            str_num = str(i)

            if len(str_num) >= 8 and str_num[0] == '1' and str_num[-1] == '7' and str_num[-6:-2] == '4239' and i % 3147 == 0:
                print(i)

    @staticmethod
    def run_59818() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=59818"""
        def check_mask(num : str) -> bool:
            if len(num) >= 4 and num[-3:-1] == '65' and '31' in num:
                return True
            return False

        res = []

        scm = 2031 * 31
        for i in range(scm, 10**9 + 1, scm):
            str_num = str(i)
            if check_mask(str_num):
                divs = Util.get_divs(i)
                if Util.is_two_pow(len(divs)):
                    res.append((i, i//2031))

        Util.output(res)

    @staticmethod
    def run_76128() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=76128"""
        res = []

        for i in range(2, 900_001):
            divs = Util.get_divs(i)
            if len(divs) > 2:
                s = divs[1]**2 + divs[-1]**2
                s_divs = Util.get_divs(s)
                if len(s_divs) == 2:
                    if len(res) < 5:
                        res.append((i, s))
                    else:
                        break

        Util.output(res)
        Util.output(res, rev=True)


def main():
    Solution.run_76128()


if __name__ == "__main__":
    main()