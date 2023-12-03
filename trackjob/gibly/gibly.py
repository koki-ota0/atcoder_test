import sys
import pandas as pd

def main(argv):
    df = pd.read_csv(argv)
    df['THI'] = 0
    for i in range(len(df)):
        a = df.iloc[i]['Altitude']
        t = df.iloc[i]['Temperature']
        h = df.iloc[i]['Humidity']
        thi = clac_THI(df.iloc[i]['Temperature'], df.iloc[i]['Humidity'])
        df.at[i, 'THI'] = thi
    # thiと高度のピアソンの席率相関係数を求める
    r = df['THI'].corr(df['Altitude'])
    print(r)

def clac_THI(Temperature, Humidity):
    THI = 0.81*Temperature + 0.01*Humidity*(0.99*Temperature - 14.3) + 46.3
    return THI

if __name__ == '__main__':
    main('test.csv')
