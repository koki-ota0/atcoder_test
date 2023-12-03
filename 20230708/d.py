"""
問題文
N1+N2頂点M辺の無向グラフがあります。
i=1,2,…,Mに対し、i番目の辺は頂点aiと頂点biを結びます。
また、以下を満たすことが保障されます。
・1≤u,v≤N1を満たす整数u,vに対し、頂点uと頂点vは連結
・N1+1≤u,v≤N1​+N2を満たす整数u,vに対し、頂点uと頂点vは連結
・頂点1と頂点N1​+N2は非連結
次の操作をちょうど1回行います。
1≤u≤N1を満たす整数uとN1​+1≤v≤N1+N2を満たす整数
vを選び、頂点uと頂点vを結ぶ辺を追加する操作後のグラフにおいて、頂点
1と頂点N1​+N2は必ず連結であることが示せます。
そこで、頂点1と頂点N1​+N2を結ぶ経路の長さ(辺の本数)の最小値をdとします。

操作で追加する辺を適切に選んだ時にありえるdの最大値を求めてください。
"""
from collections import deque
def bfs(graph, start):
    # 各頂点の訪問状態を初期化
    visited = [False] * len(graph)
    # 距離を記録する配列を初期化し、start位置の距離を0とする
    distance = [float('inf')] * len(graph)
    distance[start] = 0

    # BFSによる探索のためのキューを作成し、start位置を追加
    queue = deque([start])
    visited[start] = True

    while queue:
        # キューの先頭から頂点を取り出す
        current = queue.popleft()

        # 隣接する頂点を探索
        for neighbor in graph[current]:
            if not visited[neighbor]:
                # 隣接する頂点を未訪問状態から訪問済み状態に変更
                visited[neighbor] = True
                # 距離を更新
                distance[neighbor] = distance[current] + 1
                # 隣接する頂点をキューに追加
                queue.append(neighbor)

    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = -1
    return max(distance)

def main(N1, N2, M, graph):
    # 頂点1から最も遠い頂点を求める
    max_distance0 = bfs(graph, 0)
    max_distanceN = bfs(graph, N1+N2-1)

    # 頂点1から最も遠い頂点と頂点N1+N2から最も遠い頂点の距離が最大の場合
    print(max_distance0 + max_distanceN + 1)

# graph = [[1, 2], [0, 2], [1, 0], [4, 5], [3], [3, 6], [5]]
# main(3,4,6,graph)

N1, N2, M = map(int, input().split())
graph = [[] for _ in range(N1+N2)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
main(N1, N2, M, graph)