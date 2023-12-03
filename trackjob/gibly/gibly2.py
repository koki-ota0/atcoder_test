import sys
import pandas as pd
import numpy as np

def main(argv):
    step = argv[0]
    df = pd.read_csv(argv[1])
    columns = ['sales', 'temperature', 'THI', 'num_staff']
    if step == "step1":
        for c in columns:
            print(df.loc[:, c].mean(), df.loc[:, c].var(), df.loc[:, c].min(), df.loc[:, c].max(), sep=',')
    df = clean_df(df)
    if step == "step2":
        for i in range(len(df)):
            print(df.iloc[i]['date'], df.iloc[i]['sales'], df.iloc[i]['weather'], df.iloc[i]['temperature'], df.iloc[i]['THI'], df.iloc[i]['num_staff'], sep=',')
    df.drop('weather', axis=1, inplace=True)
    df.drop('date', axis=1, inplace=True)
    
    # 最小二乗法を用いた予測モデルの作成
    A = np.array(df.drop('sales', axis=1))
    y = np.array(df['sales'])
    x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(y)
    # 予測値を求める
    if step == "step3":
        test_df = pd.read_csv(argv[2])
        test_df = clean_df(test_df)
        test_df.drop('weather', axis=1, inplace=True)
        test_df.drop('date', axis=1, inplace=True)
        test_df.drop('sales', axis=1, inplace=True)
        test_A = np.array(test_df)
        pred = test_A.dot(x)
        for i in range(len(pred)):
            print(pred[i])

def clean_df(df):
    columns = ['sales', 'temperature', 'THI', 'num_staff']
    for c in columns:
        df[c].fillna(df[c].mean(), inplace=True)
        if c != 'sales':
            df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())
    # 天気を0,1に変換
    df['weather'].fillna(1, inplace=True)
    df['blue_sky'] = 0
    df['sunny'] = 0
    df['cloudy'] = 0
    df['rainy'] = 0
    for i in range(len(df)):
        if df.iloc[i]['weather'] == 0:
            df.at[i, 'blue_sky'] = 1
        elif df.iloc[i]['weather'] == 1:
            df.at[i, 'sunny'] = 1
        elif df.iloc[i]['weather'] == 2:
            df.at[i, 'cloudy'] = 1
        elif df.iloc[i]['weather'] == 3:
            df.at[i, 'rainy'] = 1
    return df

if __name__ == '__main__':
    main(['step2','sample.csv'])