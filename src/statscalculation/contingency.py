import numpy as np
from statscalculation.cli_utils import int_input

def data_input(row: int, col: int) -> list[list[int]]:
    data = []
    for _ in range(row):
        print(f"Please input the {_ + 1}th line of data, each figure should be seperated with space!")
        raw_data = input().split()
        while len(raw_data) != col:
            print("The length of data is inconsistent with the number of columns, please try again!")
            raw_data = input("Please enter the data \n").split()
        raw_data = [int(i) for i in raw_data]
        data.append(raw_data)
    return data


def main():
    row, col = int_input("Please enter the number of rows:"), int_input("Please enter the number of columns")
    df = (row - 1) * (col - 1)      # 自由度
    total = row * col
    data = np.array(data_input())
    # data[i][j]为第i行第j列对应的数
    # 观测值 - 预测值
    for i in range(row):
        for j in range(col):
            # estimated = data[i]  * data[j] / total
            sum_of_row_i = data[i, :].sum()
            sum_of_col_j = data[:, j].sum()
            estimated = sum_of_row_i * sum_of_col_j / total 
            diff = data[i][j] - estimated
            pass
    return 





if __name__ == "__main__":
    main()