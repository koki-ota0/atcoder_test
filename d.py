def dfs(i, j, k, H, W, grid, visited):
    # 終了条件：最後のマス(H, W)に到達した場合
    if i == H and j == W:
        return True

    # 次に探索する文字を取得
    next_char = "snuke"[(k) % 5]
    print(next_char)

    # 辺で隣接するマスを探索
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        print(ni, nj, grid)

        # 探索範囲内かつ次に探索する文字と一致し、未探索のマスの場合
        if 0 <= ni <= H and 0 <= nj <= W:
            if grid[ni][nj] == next_char:
                if not visited[ni][nj]:
                    # マスを探索済みとしてマーク
                    visited[ni][nj] = True

                    # 次のマスを探索
                    if dfs(ni, nj, k + 1, H, W, grid, visited):
                        return True

    return False

# グリッドの行数と列数を取得
H, W = map(int, input().split())

# グリッドの文字列を受け取る
grid = []
for _ in range(H):
    row = input()
    grid.append(row)

H = H - 1
W = W - 1

# 初期位置(1, 1)から探索を開始
visited = [[False] * (W+1) for _ in range(H+1)]
visited[0][0] = True  # 初期位置は探索済みとしてマーク
# grid = ["skunsek",
#         "nukesnu",
#         "ukeseku",
#         "nsnnesn",
#         "uekukku"
#         ]
if grid[0][0] != "s":
    print("No")
elif dfs(0, 0, 1, H, W, grid, visited):
    print("Yes")
else:
    print("No")
