import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(wall):
    global answer
    q = deque(virus)
    tmp = copy.deepcopy(arr)

    for i in wall:
        tmp[i[0]][i[1]] = 2

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue

            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1

    answer = max(count, answer)

n, m = map(int, input().split())
arr = []
combi = []
virus = []
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            combi.append((i, j))
        
        elif arr[i][j] == 2:
            virus.append((i, j))

wall = list(combinations(combi, 3))

for i in wall:
    bfs(i)

print(answer)
