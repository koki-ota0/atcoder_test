"""
問題文
高橋君は医者のすぬけ君から 
N 種類の薬を処方されました。
i 種類目の薬は(処方された日を含めて) 
a 
i
​
  日間、毎日 
b 
i
​
  錠ずつ飲む必要があります。また、高橋君はこれ以外の薬を飲む必要がありません。

薬を処方された日を 
1 日目とします。
1 日目以降で、初めて高橋君がその日に飲む必要がある薬が 
K 錠以下になるのは何日目かを求めてください。
"""
N, K = map(int, input().split())
medicine = []
n = 0
for i in range(N):
    a, b = map(int, input().split())
    n += b
    medicine.append([a, b])
if n <= K:
    print(1)
    exit()
medicine = sorted(medicine, reverse=True)
m = medicine[0][1]
if m > K:
    print(medicine[0][0]+1)
    exit()
i = 1
while m <= K and i < N:
    m += medicine[i][1]
    i += 1
print(medicine[i-1][0]+1)