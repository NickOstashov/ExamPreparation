#https://inf-ege.sdamgia.ru/problem?id=8094
def solution_8094():
    def sum_bin(bin_num: str ) -> int:
        """функция подсчета суммы символов в двоичном числе"""
        summ :int = 0
        for symbol in bin_num:
            summ += int(symbol)
        return summ

    def calc_new_bin(n: int) -> int:
        """функция расчета искомого числа по заданому алгоритму"""
        bin_n : str  = bin(n)[2:]   #пропускаем первые два символа '0b'
        bin_n = bin_n + str(sum_bin(bin_n) % 2)
        bin_n = bin_n + str(sum_bin(bin_n) % 2)
        return int(bin_n, 2)

    solution_num = 0 #искомое число
    n = 0   # число для расчета

    # пока искомое число меньше 43 согласно условию задачи
    while solution_num <= 43:
        solution_num = calc_new_bin(n)
        n += 1

    print(solution_num)


#https://inf-ege.sdamgia.ru/problem?id=16381
def solution_16381():
    def calc_new_value(n: int) -> int:
        """функция расчета нового числа по условию задачи"""
        bin_n : str = bin(n)[2:-1]  # убираем первые два символа и последнии
        if n % 2 == 0:
            bin_n += '01'
        else:
            bin_n += '10'
        return  int(bin_n, 2)

    n = 0           # число для расчета
    calc_value = 0  # результат расчета
    while calc_value != 2018:
        n += 1
        calc_value = calc_new_value(n)

    print(n)


#https://inf-ege.sdamgia.ru/problem?id=56505
def solution_56505():
    def sum_bin(num: int) -> int:
        """функция для подсчета суммы цифр числа num"""
        summ = 0
        while num > 0:
            summ += num % 10
            num = num // 10

        return summ

    def get_add_value(summ : int) -> str:
        """функция для выбора добавочного разряда"""
        if summ % 2 == 0:
            return '0'
        return '1'

    def calc_new_bin(num: int) -> int:
        """функция для расчета числа по условию задачи"""
        bin_n : str = bin(num)[2:]
        bin_n += get_add_value(sum_bin(int(bin_n, 2)))
        bin_n += get_add_value(sum_bin(int(bin_n, 2)))
        bin_n += get_add_value(sum_bin(int(bin_n, 2)))

        return int(bin_n, 2)

    left_bound = int(bin(123_456_789)[2:-3], 2)
    n = left_bound - 100
    calc_value = 0
    count = 0

    while calc_value <= 1_987_654_321:
        n += 1
        calc_value = calc_new_bin(n)
        if 123_456_789 <= calc_value <= 1_987_654_321:
            count += 1

    print(count)

#https://inf-ege.sdamgia.ru/problem?id=15791
def solution_15791():
    def sum_bin(bin_str: str) -> int:
        summ = 0
        for symbol in bin_str:
            summ += int(symbol)
        return summ

    def calc_new_val(n: int) -> int:
        bin_n : str = bin(n)[2:]
        bin_n += str(sum_bin(bin_n) % 2)
        bin_n += str(sum_bin(bin_n) % 2)

        return int(bin_n, 2)

    n, calc_val = 0,0
    while calc_val < 97:
        n += 1
        calc_val = calc_new_val(n)

    print(calc_val)

#https://inf-ege.sdamgia.ru/problem?id=16882
def solution_16882():
    def rev_bin(bin_str: str) -> int:
        res = ''
        for symbol in bin_str:
            if symbol == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)

    def calc_new_val(n: int) -> int:
        bin_n : str = bin(n)[2:]
        bin_n = '0'*(8-len(bin_n)) + bin_n
        return rev_bin(bin_n) - n

    n, calc_val = 0, 0
    while calc_val != 111:
        n += 1
        calc_val = calc_new_val(n)

    print(n)

def main():
    solution_16882()


if __name__ == '__main__':
    main()
