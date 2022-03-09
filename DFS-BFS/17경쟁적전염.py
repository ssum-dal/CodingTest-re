import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    q = deque(virus)

    while q:
        v, x, y, time = q.popleft()

        if time == s:
            break

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue

            if arr[nx][ny] == 0:
                q.append((v, nx, ny, time+1))
                arr[nx][ny] = v

arr = []
virus = []
n, k = map(int, input().split())

for i in range(n):
    arr.append(list(map(int, input().split())))

    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], i, j, 0))

s, X, Y = map(int, input().split())

virus.sort()
bfs()

print(arr[X-1][Y-1])

