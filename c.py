def sort_people(N, records):
    people = [(i+1, records[i][0]/(records[i][0]+records[i][1])) for i in range(N)]
    people.sort(key=lambda x: (-x[1], x[0]))
    sorted_people = [person[0] for person in people]
    return sorted_people

# 入力を受け取る
N = int(input())
records = []
for _ in range(N):
    A, B = map(int, input().split())
    records.append((A, B))

# 人々を並び替えて出力
sorted_people = sort_people(N, records)
output = " ".join(map(str, sorted_people))
print(output)