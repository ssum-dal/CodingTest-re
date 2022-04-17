import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(x)
    distance[x] = 0
    
    while q:
        v = q.popleft()

        for i in arr[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                q.append(i)


# n: 도시 수 m: 도로 수 k: 거리정보 x: 출발 도시 번호
n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [-1]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

bfs()

if not k in distance:
    print(-1)

else:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
