import sys
from collections import deque

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(a, b):
    visited[a][b] = True
    q = deque()
    q.append((a, b))
    count = 1
    people = arr[a][b]
    union = [(a, b)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue

            if not visited[nx][ny] and (l <= abs(arr[x][y] - arr[nx][ny]) <= r):
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1
                people += arr[nx][ny]
                union.append((nx, ny))

    if count > 1:
        average = people // count

        for X, Y in union:
            arr[X][Y] = average

        return True

    else:
        return False
                

            

n, l, r = map(int, input().split())
arr = []
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

while True:
    moved = False
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    moved = True

    if not moved:
        break
    else:
        answer += 1

print(answer)