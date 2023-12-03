def calculate_total_cost(dishes, prices):
    total_cost = 0
    
    for dish in dishes:
        if dish in prices:
            total_cost += prices[dish]
        else:
            total_cost += prices['default']
    
    return total_cost
 
# 入力を受け取る
N, M = map(int, input().split())
dishes = input().split()
colors = input().split()
price = list(map(int, input().split()))
prices = {}
 
# 価格を辞書に格納する
for i in range(M):
    prices[colors[i]] = price[i+1]
prices['default'] = price[0]
 
# 合計価格を計算して出力
total_cost = calculate_total_cost(dishes, prices)

print(total_cost)
