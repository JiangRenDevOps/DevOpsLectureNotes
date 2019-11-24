import csv
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame


def csv_reader_read_file(filename: str):
    with open(filename) as f:
        csv_file = csv.reader(f, delimiter=',')
        # You need to fill in some code to print the file line by line


def pandas_read_file(filename: str):
    df = pd.read_csv(filename)
    df = df.set_index("Date")
    print(df)
    return df


def compare_trend(stocks: dict):
    df = DataFrame()
    for code, stock_df in stocks.items():
        df[code] = stock_df["Adj Close"]
    df.plot()
    plt.show()


if __name__ == '__main__':
    # Let us read the AAPL and TEAM csv files and print the result out line by line

    # Let us read them again via pandas

    # Are you able to change our function and compare the trend by a given column name?

    pass


