"""
問題文
N 行 N 列のマス目が与えられます。上から i 行目、左から j 列目のマスには整数 A i,jが書かれています。ここで、
A 
i,j
​
  は 
0 か 
1 であることが保証されます。

マス目の外側のマスに書かれた整数を時計回りに 
1 個ずつずらしたときのマス目を出力してください。

ただし外側のマスとは、
1 行目、
N 行目、
1 列目、
N 列目のいずれか 
1 つ以上に属するマスの集合のことを指します。
"""

N = int(input())
A = []
for i in range(N):
    A.append(input())
B = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0:
            if j == 0:
                B[i][j] = A[i+1][j]
            else:
                B[i][j] = A[i][j-1]
        elif i == N-1:
            if j == N-1:
                B[i][j] = A[i-1][j]
            else:
                B[i][j] = A[i][j+1]
        elif j == 0:
            B[i][j] = A[i+1][j]
        elif j == N-1:
            B[i][j] = A[i-1][j]
        else:
            B[i][j] = A[i][j]
for i in range(N):
    for j in range(N):
        print(B[i][j], end="")
    print()


        