import sys
from itertools import combinations
import copy

input = sys.stdin.readline

def isPossible(w):
    
    tmp = copy.deepcopy(arr)

    for i in w:
        tmp[i[0]][i[1]] = 'O'
    
    for i in teacher:
        x, y = i[0], i[1]

        while x >= 0:
            if tmp[x][y] == 'O':
                break
            if tmp[x][y] == 'S':
                return 'NO'

            x -= 1
        
        x, y = i[0], i[1]
        while x < n:
            if tmp[x][y] == 'O':
                break
            if tmp[x][y] == 'S':
                return 'NO'

            x += 1

        x, y = i[0], i[1]
        while y >= 0:
            if tmp[x][y] == 'O':
                break
            if tmp[x][y] == 'S':
                return 'NO'

            y -= 1

        x, y = i[0], i[1]
        while y < n:
            if tmp[x][y] == 'O':
                break
            if tmp[x][y] == 'S':
                return 'NO'

            y += 1

    return 'YES'


n = int(input())
arr = []
combi = []
teacher = []

for _ in range(n):
    arr.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))
        
        elif arr[i][j] == 'X':
            combi.append((i, j))

wall = list(combinations(combi, 3))

for i in wall:
    answer = isPossible(i)

    if answer == 'YES':
        break

print(answer)