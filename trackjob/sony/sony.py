import sys
import time
# レストラン情報 ID x y
# 祝日情報 MM-DD
# 最低注文金額の設定 YYYY-MM-DD HH:MM set_min ID money
# 送料無料金額の設定 YYYY-MM-DD HH:MM set_free ID money
# 休業日の設定 YYYY-MM-DD HH:MM close_day ID day
# 休業日の解除 YYYY-MM-DD HH:MM open_day ID day
# 休業時間の設定 YYYY-MM-DD HH:MM close_time ID time
# 休業時間の解除 YYYY-MM-DD HH:MM open_time ID time
# 注文 YYYY-MM-DD HH:MM order ID money x y
# 休業日の時は 日時および"ERROR CLOSED DAY日時および"
# 休業時間の時は 日時および"ERROR CLOSED TIME日時および"
# 最低注文金額に達していない時は 日時および"ERROR INSUFFICIENT日時および"
# 注文が受理されたら売り上げに計上する
# 送料は0-100m:300円、100-1000m:600円、1000m-10000m:900円、10000m-:1200円
# 売上の集計 YYYY-MM-DD HH:MM calculate レストランID YYYY-MM-DD HH:MM YYYY-MM-DD HH:MM
# ->SALESと売上の合計をスペース区切りで出力

# 入力、1: 祝日数n,レストランの店舗数m
# 2: n行の祝日の日付
# 3: m行のレストランの情報
# 4: クリエ(注文、休業日設定、休業時間設定、休業日解除、休業時間解除、最低注文金額、送料無料金額の設定)

def main(lines):
    holidays = []
    restaurants = {}
    n, m = map(int, lines[0].split())
    for i in range(n):
        holidays.append(lines[i+1])
    for i in range(m):
        id, x, y = lines[i+n+1].split()
        restaurants[id] = {
            "place":[int(x), int(y)],
            "min":0,
            "free":1000000,
            "close_day":[],
            "close_time":[],
            "profit":[]
            }
    i = n + m + 1
    while i < len(lines):
        line = lines[i].split()
        q_time = line[0] + " " + line[1]
        id = line[3]
        restaurant = restaurants[id]
        if line[2] == "order":
            order_cost = int(line[4])
            x = int(line[5])
            y = int(line[6])
            profit = order(q_time, id, order_cost, x, y, holidays, restaurant)
            # 売り上げを計上
            if profit == None:
                pass
            else:
                restaurants[id]['profit'] += [[q_time, profit]]
        
        # 送料無料の設定
        elif line[2] == "set_free":
            restaurants[id]["free"] = int(line[4])

        # 最低注文金額の設定
        elif line[2] == "set_min":
            restaurants[id]["min"] = int(line[4])

        # 休業日の設定
        elif line[2] == "close_day":
            if line[4] not in restaurants[id]["close_day"]:
                restaurants[id]["close_day"] += [line[4]]

        # 休業日の解除
        elif line[2] == "open_day":
            if line[4] in restaurants[id]["close_day"]:
                restaurants[id]["close_day"].remove(line[4])

        # 休業時間の設定
        elif line[2] == "close_time":
            restaurants[id]["close_time"] = [line[4], line[5]]

        # 休業時間の解除
        elif line[2] == "open_time":
            s = time.strptime(line[4], '%H:%M')
            e = time.strptime(line[5], '%H:%M')
            if restaurants[id]["close_time"] == []:
                pass
            else:
                c_s = time.strptime(restaurants[id]["close_time"][0], '%H:%M')
                c_e = time.strptime(restaurants[id]["close_time"][1], '%H:%M')
                if (s <= c_s <= c_e <= e):
                    restaurants[id]["close_time"] = []
                elif (c_s <= s <= c_e <= e):
                    restaurants[id]["close_time"] = [time.strftime('%H:%M', c_s), time.strftime('%H:%M', s)]
                elif (s <= c_s <= e <= c_e):
                    restaurants[id]["close_time"] = [time.strftime('%H:%M', e), time.strftime('%H:%M', c_e)]
                else:
                    pass

        # 売り上げの集計
        elif line[2] == "calculate":
            start = time.strptime(line[4] + " " + line[5], '%Y-%m-%d %H:%M')
            end = time.strptime(line[6] + " " + line[7], '%Y-%m-%d %H:%M')
            profit = 0
            for j in range(len(restaurant["profit"])):
                profit_time = time.strptime(restaurant["profit"][j][0], '%Y-%m-%d %H:%M')
                if start <= profit_time <= end:
                    profit += restaurant["profit"][j][1]
            print(q_time, "SALES", profit)
        
        i += 1


def calc_send_cost(x, y, x2, y2):
    # 送料を計算
    distance =  ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    if distance < 100:
        send_cost = 300
    elif distance < 1000:
        send_cost = 600
    elif distance < 10000:
        send_cost = 900
    else:
        send_cost = 1200
    return send_cost

def is_closed_day(q_time, holidays, restaurant):
    # 休業日かどうか
    if restaurant["close_day"] == []:
        return False
    else:
        for day in restaurant["close_day"]:
            if (day == "HOLIDAY") & (q_time[5:10] in holidays):
                    return True
            elif (day == "MON") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 0):
                return True
            elif (day == "TUE") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 1):
                return True
            elif (day == "WED") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 2):
                return True
            elif (day == "THU") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 3):
                return True
            elif (day == "FRI") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 4):
                return True
            elif (day == "SAT") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 5):
                return True
            elif (day == "SUN") & (time.strptime(q_time, '%Y-%m-%d %H:%M').tm_wday == 6):
                return True
        return False

def is_closed_time(q_time, restaurant):
    # 休業時間かどうか
    if restaurant["close_time"] == []:
        return False
    else:
        if time.strptime(restaurant["close_time"][0], '%H:%M') <= time.strptime(q_time[11:], '%H:%M') <= time.strptime(restaurant["close_time"][1], '%H:%M'):
            return True
        else:
            return False

def order(q_time, id, order_cost, x, y, holidays, restaurant):
    # 休業日かどうか
    if is_closed_day(q_time, holidays, restaurant):
        print(q_time, "ERROR CLOSED DAY")
        return
    # 休業時間かどうか
    if is_closed_time(q_time, restaurant):
        print(q_time, "ERROR CLOSED TIME")
        return
    
    # 最低注文金額に達しているかどうか
    if order_cost < restaurant["min"]:
        print(q_time, "ERROR INSUFFICIENT")
        return 
    
    # 送料無料かどうか
    if order_cost >= restaurant["free"]:
        free = True
    else:
        free = False

    # 送料を計算
    place = restaurant["place"]
    send_cost = calc_send_cost(x, y, place[0], place[1])

    if free:
        print(q_time, order_cost)
        return order_cost - send_cost
    else:
        print(q_time, order_cost + send_cost)
        return order_cost

# サンプルデータ
# 10 10
# 03-13
# 03-14
# 03-16
# 05-27
# 08-08
# 09-08
# 11-03
# 11-17
# 12-20
# 12-25
# wGVKq -236 530
# bcSdD -885 -469
# EiUvv 885 -935
# biBwv -868 -628
# ZOypa 678 -313
# dPjQJ -658 -11
# DrzPc -1000 -483
# xHsUa -706 442
# cZrDg 860 741
# DHSKg -170 191
# 2020-04-11 17:22 order ZOypa 21438 -286 -57
# 2023-02-22 17:35 order biBwv 79110 718 190
# 2025-04-15 08:09 set_free biBwv 6375
# 2035-12-02 22:08 order DHSKg 39617 -734 104
# 2037-03-24 12:15 order biBwv 63161 652 538
# 2037-08-19 08:34 set_free xHsUa 3864
# 2038-02-01 15:55 set_min ZOypa 4219
# 2038-05-19 16:52 close_day cZrDg FRI
# 2039-02-05 18:52 order wGVKq 31048 98 -175
# 2039-12-29 03:52 order bcSdD 75809 -256 -228
# 2041-08-28 17:45 close_day cZrDg HOLIDAY
# 2041-12-18 22:13 order biBwv 76619 -818 975
# 2042-10-21 05:07 order ZOypa 86651 359 -134
# 2043-08-27 23:22 order biBwv 36676 936 -157
# 2044-08-23 17:39 order ZOypa 13903 125 -957
# 2045-01-09 04:12 order xHsUa 8117 -247 -533
# 2045-05-23 14:54 set_free ZOypa 2106
# 2047-02-03 01:41 close_time biBwv 06:45 17:21
# 2047-11-15 11:25 set_free dPjQJ 895
# 2048-05-09 11:20 order DrzPc 81885 -463 -683
# 2048-06-13 16:04 order dPjQJ 33329 -618 197
# 2050-04-22 18:11 order DHSKg 21913 -882 -799
# 2054-03-03 14:34 set_free DrzPc 9374
# 2055-03-19 21:51 close_day DrzPc FRI
# 2056-03-05 13:59 order DrzPc 3988 268 65
# 2060-01-24 01:53 open_time biBwv 05:30 23:55
# 2061-01-15 18:40 order ZOypa 23466 -766 474
# 2061-04-29 06:31 close_day xHsUa TUE
# 2065-11-19 17:12 set_min EiUvv 775
# 2069-03-11 05:31 order xHsUa 16559 788 305
# 2072-02-13 21:23 open_day DHSKg SAT
# 2073-10-30 12:47 order biBwv 28719 -517 667
# 2073-11-22 02:47 set_free wGVKq 5528
# 2074-01-27 13:03 close_day ZOypa HOLIDAY
# 2074-10-19 10:37 close_day bcSdD WED
# 2076-10-15 22:37 order EiUvv 93628 -559 416
# 2077-02-23 15:07 calculate DHSKg 2077-11-19 05:26 2095-06-26 21:20
# 2077-11-18 23:03 open_time wGVKq 02:48 12:05
# 2079-03-02 10:40 order cZrDg 15891 -44 488
# 2086-04-09 00:32 open_day ZOypa HOLIDAY
# 2086-09-08 05:53 open_time bcSdD 18:24 21:02
# 2087-01-17 22:48 set_free wGVKq 5966
# 2089-01-25 23:54 set_min DrzPc 8434
# 2091-02-02 05:08 order ZOypa 85471 -810 -849
# 2092-04-29 04:05 order EiUvv 38937 -395 657
# 2093-04-15 04:48 order bcSdD 65814 969 -618
# 2095-04-22 00:23 open_time wGVKq 15:22 22:20
# 2096-01-17 22:16 order xHsUa 43285 253 593
# 2096-07-05 04:33 close_time bcSdD 08:36 14:11
# 2098-04-12 17:27 order DrzPc 1482 -865 850


if __name__ == '__main__':
    lines = []
    # サンプルデータでテスト
    with open('sample.txt') as f:
        lines = f.readlines()
    main(lines)
