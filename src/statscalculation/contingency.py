import numpy as np
from scipy.stats import chi2
from statscalculation.cli_utils import int_input, float_input

def data_input(r: int, c: int):
    '''
        接受r c参数返回np.array数组
        输入函数与cli_utils中定义的有所不同
        故单独定义
    '''
    data = []
    print("Attention, each figure should be seperated by space!")
    for _ in range(r):
        if _ == 1:
            print(f"Please enter the 1st row of data:", end='')
        elif _ == 2:
            print(f"Please enter the 2nd row of data:", end='')
        elif _ == 3:
            print(f"Please enter the 3rd row of data:", end='')
        else:
            print(f"Please enter the {_ + 1}th row of data:", end='')
        raw_data = input().split()
        while len(raw_data) != c:
            print("The length of data is inconsistent with the number of columns, please try again!")
            raw_data = input("Please enter the data:", end='').split()
        raw_data = [int(i) for i in raw_data]
        data.append(raw_data)
    return np.array(data)


def main():
    # 构造临界值
    alpha = float_input("Please enter the significance level:")
    r, c = int_input("Please enter the number of rows:"), int_input("Please enter the number of columns")
    total = r * c
    df = (r - 1) * (c - 1)      # 自由度
    critical_value = chi2.ppf(1 - alpha, df)
    data = data_input()
    # data[i][j]为第i行第j列对应的数
    # 观测值 - 预测值
    x_2 = 0
    for i in range(r):
        for j in range(c):
            sum_of_r_i = data[i, :].sum()
            sum_of_c_j = data[:, j].sum()
            estimated = sum_of_r_i * sum_of_c_j / total 
            diff = data[i, j] - estimated
            x_2 += (diff ** 2 / estimated)
    if x_2 >= critical_value:
        print(f"test statistic {x_2} >= critical value {critical_value} -> reject H₀")
    else: 
        print(f"test statistic {x_2} < critical value {critical_value} -> fail to reject H₀")
    return "Independency test ends, press any key to exit."

if __name__ == "__main__":
    main()