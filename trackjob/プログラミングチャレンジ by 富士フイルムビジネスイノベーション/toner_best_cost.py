"""
富士フイルムビジネスイノベーションでは、 オフィスワーク用の複合機を開発しています。 
複合機は印刷を行なう際の現像剤であるトナーを消費し、 トナー残量がなくなるとトナーカートリッジを交換する必要があります。
track 社は富士フイルムビジネスイノベーションの複合機を A台導入することにし、それぞれの複合機で日々消費されるトナー量を見積もりました。 以下の問
題文を読んで、トナーカートリッジの購入を最適に行なった時の、 トナーカートリッジの購入と保管にかかるコストの和を見積もってください。

問題文
track 社は日付に複合機を A台購入し、 日付 D まで運用します。
最初は各複合機のトナー残量はBで、 i台目の複合機は毎日トナーを ci 消費します。 
トナー残量が 0 になった際は即座にあらかじめ購入しておいたカートリッジと交換する必要があります。 
交換後のトナー残量は B となり、その日の消費量がまだ ci に達していなければ引き続き消費されます。
カートリッジの購入費用は、(購入数)×(単価 X) + (配送料 Y)で計算され、 単価と配送料は購入数や購入日に依らず一定です。 
従ってカートリッジをまとめて購入した方がお得ですが、 カートリッジの置き場所の確保が必要なので、 保管にもコストがかかります。
具体的には(カートリッジ交換カートリッジ購入日)xZが保管コストとしてかかります。
ただし、 交換日と購入日は整数です。
A, B, C, X, Y, Z を入力として受け取り、カートリッジの購入費用と保管コストの和の最小値を計算するプログラムを作成してください。
ただし、
・日付1にもトナーは消費されます。
・日付eに購入したカートリッジを日付eに交換に利用することは可能です。
・日付eの終わりにトナー残量がちょうど0になった場合(=トナー残量が0となると同時にその日の消費量がci に達した場合)、カートリッジの交換は日付e+1ではなく日付e に行なうものとします。
・日付 D の終わりにトナー残量がちょうど 0 になった場合、交換は不要です。
計算過程でのオーバーフローに注意してください。
この問題のテストケースは基本実装、 応用実装という2種類に分類されていて、 それぞれ 50 点ずつを占めます。 
基本実装のテストケースはD=16、 応用実装のテストケースはD=1000 を満たします。 
満点を取るのが難しい場合は、 基本実装のテストケースのみに正答できるプログラムを作成して部分点を取得することを推奨します。
"""
from re import T
import sys

def calculate_cost(A, B, D, c, X, Y, Z):
    remaining_toner = [B] * A  # 各トナーの残量を保持するリスト
    total_cost = 0
    
    purchase_n = 0
    purchase_date = []

    for day in range(1, D+1):
        tmp_n = 0
        purchase = False # その日に買う必要があるか
        for i in range(A):
            remaining_toner[i] -= c[i]  # 各トナーの消費量を適用

            if day == D:
                while remaining_toner[i] < 0:
                    purchase = True
                    remaining_toner[i] += B
                    tmp_n += 1
            else:
                while remaining_toner[i] <= 0:
                    purchase = True
                    remaining_toner[i] += B
                    tmp_n += 1
        
        if purchase:
            purchase_date.append([day, tmp_n])
            purchase_n += tmp_n
    num_buy_day = len(purchase_date)

    if purchase_n > 0:
        if Y <= Z: # 補完費が高い場合
            total_cost  += (purchase_n * X) + (Y * num_buy_day)
        else:
            low_days = max(1, Y//Z - 1)
            while len(purchase_date) > 1:
                tmp1 = purchase_date.pop(0)
                while len(purchase_date)>0:
                    tmp2 = purchase_date[0]
                    if tmp2[0] - tmp1[0] <= low_days:
                        total_cost += (tmp2[0] - tmp1[0]) * Z * tmp2[1]
                        num_buy_day -= 1
                        purchase_date.pop(0)
                    else:
                        break
            total_cost  += (purchase_n * X) + (Y * num_buy_day)

    return total_cost


def main(lines):
    # A, B, D = map(int, lines[0].split())
    # c = list(map(int, lines[1].split()))
    # X, Y, Z = map(int, lines[2].split())
    # cost = calculate_cost(A, B, D, c, X, Y, Z)
    # print(cost)
    print(6//2)

if __name__ == '__main__':
    # lines = []
    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))
    lines = 0
    main(lines)
