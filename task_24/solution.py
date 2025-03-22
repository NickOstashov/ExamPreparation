class Util:
    @staticmethod
    def get_file_text(file_path : str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            return text
        except FileNotFoundError:
            return ""
        except Exception as e:
            return ""

    @staticmethod
    def get_file_lines(file_path: str) -> list:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.readlines()
            return text
        except FileNotFoundError:
            return []
        except Exception as e:
            return []

    @staticmethod
    def is_first_half(symbol: str) -> bool:
        if not symbol.isalpha():
            return False
        symbol = symbol.upper()

        return 'A' <= symbol <= 'M'


class Solution:
    @staticmethod
    def run_27421() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=27421"""
        line = Util.get_file_text("/Users/Nick/Desktop/ExamPreparation/task_24/files/27421_demo.txt")
        cnt, max_cnt = 1, 0

        for i in range(len(line) - 1):
            if line[i] != line[i + 1]:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1

        print(max_cnt)

    @staticmethod
    def run_27686() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=27686"""
        line = Util.get_file_text("/Users/Nick/Desktop/ExamPreparation/task_24/files/27686_demo.txt")
        cnt, max_cnt = 1, 0

        for i in range(len(line) - 1):
            if line[i] == "X" and line[i + 1] == "X":
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1

        print(max_cnt)

    @staticmethod
    def run_56524() -> None:
        """
        https://inf-ege.sdamgia.ru/problem?id=56524
        Проблемы задачи
        * Нужно знать символ, который образует самую длинную строку
        * Нужно знать количество символов в этой строке
        * Нужно сравнивать эту информацию в разных строках
        """

        lines = Util.get_file_lines("/Users/Nick/Desktop/ExamPreparation/task_24/files/56524_demo.txt")


        gmax_cnt = -1
        max_sym_cnt = 0

        for i in range(len(lines)):
            line = lines[i]
            lmax_cnt, sym, cnt = -1, line[0], 1
            tmp_dict = dict()

            # в цикле находим локальный максимум
            for j in range(len(line) - 1):
                if not line[j] in tmp_dict:
                    tmp_dict[line[j]] = 0

                tmp_dict[line[j]] += 1

                if line[j] == line[j + 1]:
                    cnt += 1
                else:
                    if lmax_cnt < cnt:
                        sym = line[j]
                        lmax_cnt = cnt

                    cnt = 1

            # условия смены глобального максимума
            if lmax_cnt > gmax_cnt:
                gmax_cnt = lmax_cnt
                max_sym_cnt = tmp_dict.get(sym)
            elif lmax_cnt == gmax_cnt and tmp_dict.get(sym) > max_sym_cnt:
                max_sym_cnt = tmp_dict.get(sym)

        print(max_sym_cnt)

    @staticmethod
    def run_59847() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=59847"""
        line = Util.get_file_text("/Users/Nick/Desktop/ExamPreparation/task_24/files/59847_demo.txt")
        max_cnt = 0
        left = 0

        w_cnt, rng_cnt = 0, 0
        len_l = len(line)
        for right in range(len_l - 1):

            if line[right] == "W" and line[right + 1] == "W":
                w_cnt += 1

            while w_cnt > 100:
                if line[left] == "W" and line[left + 1] == "W":
                    w_cnt -= 1
                left += 1

            if w_cnt == 100:
                rng_cnt = right - left + 2
                if rng_cnt > max_cnt:
                    max_cnt = rng_cnt

        print(max_cnt)

    @staticmethod
    def run_68257() -> None:
        """https://inf-ege.sdamgia.ru/problem?id=68257"""

        line = Util.get_file_text("/Users/Nick/Desktop/ExamPreparation/task_24/files/68257_demo.txt")
        max_cnt = 0

        for left in range(len(line) - 1):
            if not Util.is_first_half(line[left]):
                continue

            right = left + 1
            rng_cnt = 1

            while right < len(line) - 1 and line[left] != line[right]:
                rng_cnt += 1
                right += 1

            if rng_cnt > max_cnt:
                # + 1 потому что символ line[right] не посчитался
                max_cnt = rng_cnt + 1

        print(max_cnt)


def main():
    Solution.run_56524()


if __name__ == "__main__":
    main()